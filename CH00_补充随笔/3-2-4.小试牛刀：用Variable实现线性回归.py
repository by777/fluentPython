# -*- coding: utf-8 -*-
# @TIME : 2021/3/20 20:34
# @AUTHOR : Xu Bai
# @FILE : 3-2-4.小试牛刀：用Variable实现线性回归.py
# @DESCRIPTION :
import os

import torch as t
from matplotlib import pyplot as plt
from torch.autograd import Variable as V

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
t.manual_seed(1000)


def get_fake_data(batch_size=8):
    """
    y = x * 2 + 3 加上一些噪声
    """
    x = t.rand(batch_size, 1) * 20
    y = x * 2 + (1 + t.randn(batch_size, 1)) * 3
    return x, y


if __name__ == '__main__':
    # x, y = get_fake_data()
    # plt.scatter(x.squeeze().numpy(), y.squeeze().numpy())
    # plt.show()
    w = V(t.rand(1, 1), requires_grad=True)
    b = V(t.zeros(1, 1), requires_grad=True)
    lr = .001
    for ii in range(8000):
        x, y = get_fake_data()
        x, y = V(x), V(y)
        # forward
        y_pred = x.mm(w) + b.expand_as(y)
        loss = 0.5 * (y_pred - y) ** 2
        loss = loss.sum()
        # backward
        loss.backward()
        # 更新参数

        w.data.sub_(lr * w.grad.data)
        b.data.sub_(lr * b.grad.data)
        # 梯度清零
        w.grad.data.zero_()
        b.grad.data.zero_()
        if ii % 1000 == 0:
            x = t.arange(0, 20).view(-1, 1).float()
            y = x.mm(w.data) + b.expand_as(x)
            plt.plot(x.detach().numpy(), y.detach().numpy())  # pred
            x2, y2 = get_fake_data(batch_size=20)
            plt.scatter(x2.numpy(), y2.numpy())
            plt.xlim(0, 20)
            plt.ylim(0, 41)
            plt.show()
            plt.pause(0.5)
    print(w.data.item(), b.data.item())
