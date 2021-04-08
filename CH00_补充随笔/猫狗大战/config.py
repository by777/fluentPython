# -*- coding: utf-8 -*-
# @TIME : 2021/3/29 20:42
# @AUTHOR : Xu Bai
# @FILE : config.py
# @DESCRIPTION :
import warnings

import torch as t


class DefaultConfig(object):
    env = 'default'  # visdom环境
    model = 'AlexNet'  # 名字必须与models/__init__.py中名字一致
    train_data_root = './data/train/'
    test_data_root = './data/test/'
    load_model_path = None  # 加载预训练模型的路径，为None代表不加载
    batch_size = 16
    use_gpu = False
    num_workers = 0
    print_freq = 20  # print info every N batch
    debug_file = './tmp/debug'  # if os.path.exists(debug_file), enter ipdb
    result_file = 'result.csv'
    max_epoch = 10
    lr = .1  # initial learning rate
    lr_decay = .95  # when val_loss increase, lr = lr * lr_decay
    weight_decay = 1e-4  # loss function

    def _parse(self, **kwargs):
        """根据字典kwargs 更新 config参数"""
        for k, v in kwargs.items():
            if not hasattr(self, k):
                warnings.warn('Warning: opt has not attribute %s' % k)
            setattr(self, k, v)
        opt.device = t.device('cuda') if opt.use_gpu else t.device('cpu')
        print('using config:')
        for k, v in self.__class__.__dict__.items():
            if not k.startswith('_'):
                print(k, getattr(self, k))


opt = DefaultConfig()
