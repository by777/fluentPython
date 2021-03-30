# -*- coding: utf-8 -*-
# @TIME : 2021/3/29 20:58
# @AUTHOR : Xu Bai
# @FILE : main.py
# @DESCRIPTION :
import os

import torch as t
from torch.utils.data import DataLoader
from torchnet import meter
from tqdm import tqdm
import fire
import models
from config import opt
from data.dataset import DogCat
from utils.visualize import Visualizer


def train(**kwargs):
    opt._parse(**kwargs)
    vis = Visualizer(opt.env)

    # step1: 模型
    model = getattr(models, opt.model)()
    if opt.load_model_path:
        model.load(opt.load_model_path)
    if opt.use_gpu:
        model.cuda()

    # step2: 数据
    train_data = DogCat(opt.train_data_root, train=True)
    val_data = DogCat(opt.train_data_root, train=False)
    train_dataloader = DataLoader(
        train_data,
        opt.batch_size,
        shuffle=True,
        num_workers=opt.num_workers
    )
    val_dataloader = DataLoader(
        val_data,
        opt.batch_size,
        shuffle=False,
        num_workers=opt.num_workers
    )

    # step3: 目标函数和优化器
    criterion = t.nn.CrossEntropyLoss()
    lr = opt.lr
    optimizer = t.optim.Adam(
        model.parameters(),
        lr=lr,
        weight_decay=opt.weight_decay
    )

    # step4: 统计指标：平滑处理之后的损失，还有混淆矩阵
    loss_meter = meter.AverageValueMeter()
    confusion_matrix = meter.ConfusionMeter(2)
    previous_loss = 1e10

    # step5: 训练
    for epoch in range(opt.max_epoch):
        loss_meter.reset()
        confusion_matrix.reset()
        for ii, (data, label) in tqdm(enumerate(train_dataloader)):
            # 训练模型参数
            input = data.to(opt.device)
            target = label.to(opt.device)
            optimizer.zero_grad()
            score = model(input)
            loss = criterion(score, target)
            loss.backward()
            optimizer.step()

            # 更新统计指标和可视化
            loss_meter.add(loss.item())
            # detach 一下更安全保险
            confusion_matrix.add(score.detach(), target.detach())
            if (ii + 1) % opt.print_freq == 0:
                vis.plot('loss', loss_meter.value()[0])
                # 进入debug模式
                if os.path.exists(opt.debug_file):
                    import ipdb
                    ipdb.set_trace()
        model.save()
        # 计算验证集上的指标和可视化
        # validate and visualize
        val_cm, val_accuracy = val(model, val_dataloader)
        vis.plot('val_accuracy', val_accuracy)
        vis.log("epoch:{epoch},lr:{lr},loss:{loss},train_cm:{train_cm},val_cm:{val_cm}".format(
            epoch=epoch, loss=loss_meter.value()[0], val_cm=str(val_cm.value()), train_cm=str(confusion_matrix.value()),
            lr=lr))
        # update learning rate
        if loss_meter.value()[0] > previous_loss:
            lr = lr * opt.lr_decay
            # 第二种降低学习率的方法:不会有moment等信息的丢失
            for param_group in optimizer.param_groups:
                param_group['lr'] = lr

        previous_loss = loss_meter.value()[0]


# 被该语句 wrap 起来的部分将不会track 梯度。
@t.no_grad()
def val(model, dataloader):
    """
    计算模型在验证集上的准确率等信息用以辅助训练
    :param kwargs:
    :return:
    """
    # 把模型置于验证模式
    model.eval()
    confusion_matrix = meter.ConfusionMeter(2)
    for ii, (val_input, label) in tqdm(enumerate(dataloader)):
        val_input = val_input.to(opt.device)
        score = model(val_input)
        confusion_matrix.add(score.detach().squeeze(), label.type(t.LongTensor))
    model.train()
    cm_value = confusion_matrix.value()
    accuracy = 100. * (cm_value[0][0] + cm_value[1][1]) / (cm_value.sum())
    return confusion_matrix, accuracy


@t.no_grad()
def test(**kwargs):
    opt._parse(kwargs)

    # configure model
    model = getattr(models, opt.model)().eval()
    if opt.load_model_path:
        model.load(opt.load_model_path)
    model.to(opt.device)


def help():
    print("""
        需要可视化：python -m visdom.server 启动visdom服务
        usage: python file.py <function> [--args=value]
        <function> := train|test|help
        example:
            python {0} train --'env0701' --lr=0.01
            python {0} test --dataset='path/to/dataset/root/'
            python {0} help
            available  args:
    """.format(__file__))
    from inspect import getsource
    source = (getsource(opt.__class__))
    print(source)


def write_csv(results, file_name):
    import csv
    with open(file_name, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'label'])
        writer.writerows(results)


if __name__ == '__main__':
    fire.Fire()
