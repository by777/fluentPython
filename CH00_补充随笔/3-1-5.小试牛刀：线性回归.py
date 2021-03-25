# -*- coding: utf-8 -*-
# @TIME : 2021/3/20 10:54
# @AUTHOR : Xu Bai
# @FILE : 3-1-5.小试牛刀：线性回归.py
# @DESCRIPTION :
import os

import torch as t

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
from matplotlib import pyplot as plt

"""线性回归的表达式是y=wx + b +c
loss = 1 / 2 * sum{[y^ - (wx + b)]**2}"""
t.manual_seed(1000)


def get_fake_data(batch_size=8):
    """
    产生随机数据： y = 2x + 3,加上一些噪声
    :param batch_size:
    :return:
    """
    x = t.rand(batch_size, 1) * 20

    y = x * 2 + (1 + t.randn(batch_size, 1)) * 3
    return x, y


if __name__ == '__main__':

    x, y = get_fake_data()
    plt.scatter(x.squeeze().numpy(), y.squeeze().numpy())
    plt.show()
    print('随机初始化参数')
    w = t.rand(1, 1)
    b = t.zeros(1, 1)
    lr = .001
    for ii in range(10000):
        x, y = get_fake_data()
        # forward: 计算loss
        # y^ = w * x + b

        y_pred = x.mm(w) + b.expand_as(y)
        loss = 0.5 * (y_pred - y) ** 2
        loss = loss.sum()
        # backward: 手动计算梯度
        dloss = 1
        dy_pred = dloss * (y_pred - y)
        dw = x.t().mm(dy_pred)
        db = dy_pred.sum()
        # 更新参数
        w.sub_(lr * dw)
        b.sub_(lr * db)

        if ii % 1000 == 0:
            x = t.arange(0, 20.0).view(-1, 1)
            y = x.mm(w) + b.expand_as(x)
            plt.plot(x.numpy(), y.numpy())  # 预测的
            x2, y2 = get_fake_data(batch_size=20)
            plt.scatter(x2.numpy(), y2.numpy())
            plt.xlim(0, 20)
            plt.ylim(0, 41)
            plt.show()
            plt.pause(0.5)
            print(w.item(), b.item())
