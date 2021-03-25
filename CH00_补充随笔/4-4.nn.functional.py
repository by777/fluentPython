# -*- coding: utf-8 -*-
# @TIME : 2021/3/25 19:37
# @AUTHOR : Xu Bai
# @FILE : 4-4.nn.functional.py
# @DESCRIPTION :
"""
nn中还有一个很常用的模块：functional。
nn中的大部分layer在functional中都有一个与之对应的函数。
functional与Module的区别在于：
    Module中实现的layer是一个特殊的类：都是由class layer(Module)定义，会自动提取可学习的参数，
    而functional的函数更像是纯函数
"""
import torch as t
from torch import nn
from torch.autograd import Variable as V
from torch.nn import functional as F

input = V(t.randn(2, 3))
model = nn.Linear(3, 4)
output1 = model(input)
output2 = F.linear(input, model.weight, model.bias)
print(output1 == output2)
print('*********什么时候用Module或者function？*********')
print('如果模型有可学习的参数，最好用Module，否则都可以用，在性能上没有显著差异\n'
      '激活函数（tanh、sigmoid、ReLU）、MaxPool等没有可学习的参数，可以用对应的functional，\n'
      '但dropout分训练阶段和测试、建议nn.Dropout而不是nn.functional')


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = F.pool(F.relu(self.conv1(x)), 2)
        x = F.pool(F.relu(self.conv2(x)), 2)
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        return x


print('不具备可学习参数的层，将它们用函数代替，这样可以不放在构造函数__init__里'
      '有可学习参数的模块，也可以用functional代替，但是需要手动定义参数parameter，如:')


class MyLinear(nn.Module):
    def __init__(self):
        super(MyLinear, self).__init__()
        self.weight = nn.Parameter(t.randn(3, 4))
        self.bias = nn.Parameter(t.zeros(3))

    def forward(self):
        pass
        # return F.linear(input,weight,bias)
