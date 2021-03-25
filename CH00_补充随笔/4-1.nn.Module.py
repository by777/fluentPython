# -*- coding: utf-8 -*-
# @TIME : 2021/3/20 21:21
# @AUTHOR : Xu Bai
# @FILE : 4-1.nn.Module.py
# @DESCRIPTION :
import torch as t
from torch import nn
from torch.autograd import Variable as V
from torch.nn import Module


class Linear(Module):
    """实现全连接层"""

    def __init__(self, in_features, out_features):
        super(Linear, self).__init__()
        # Parameter是一特殊的variable,但默认需要求导
        self.w = nn.Parameter(t.randn(in_features, out_features))
        self.b = nn.Parameter(t.rand(out_features))

    def forward(self, x):
        x = x.mm(self.w)
        return x + self.b.expand_as(x)


class Perceptron(Module):
    """
    多层感知机
    """

    def __init__(self, in_features, hidden_features, out_features):
        super(Perceptron, self).__init__()
        self.layer1 = Linear(in_features, hidden_features)  # 这是上面定义的
        self.layer2 = Linear(hidden_features, out_features)

    def forward(self, x):
        x = self.layer1(x)
        x = t.sigmod(x)
        return self.layer2(x)


if __name__ == '__main__':
    layer = Linear(4, 3)
    input = V(t.randn(2, 4))
    print('注意上边的维度，输入的维度要一致，网络要求输入4个维度输出3个维度，所以输入的数据应该第二维是4')
    output = layer(input)
    print(output)
    for name, parameters in layer.named_parameters():
        print(name, parameters)  # w and b

    perceptron = Perceptron(3, 4, 1)
    for name, parameters in perceptron.named_parameters():
        print(name, parameters)
