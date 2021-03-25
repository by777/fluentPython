# -*- coding: utf-8 -*-
# @TIME : 2021/3/25 10:32
# @AUTHOR : Xu Bai
# @FILE : 4-2-2.激活函数.py
# @DESCRIPTION :
import torch as t
from torch import nn
from torch.autograd import Variable as V

print('#' * 50, '补充', '#' * 50)
print('inplace设置为True，它会把输出直接覆盖到输入中，可以节省内存。之所以可以覆盖是因为在计算Relu反向传播时，只需要根据输出就可以推算出反向传播的速度'
      '但只有少数的autograd支持inplace操作，如variable.sigmoid_()。除非你明确的知道自己要做什么，否则一般不要用inplace')
relu = nn.ReLU(inplace=True)
input = V(t.randn(2, 3))
ouput = relu(input)
print(ouput)

print('***使用Sequential构建网络层的三种方法***')
# print('方法1')
net1 = nn.Sequential()
net1.add_module('conv', nn.Conv2d(3, 3, 3))
net1.add_module('batchnorm', nn.BatchNorm2d(3))
net1.add_module('activation_layer', nn.ReLU())
# print('方法2')
net2 = nn.Sequential(
    nn.Conv2d(3, 3, 3),
    nn.BatchNorm2d(3),
    nn.ReLU()
)
# print('方法3')
from collections import OrderedDict

net3 = nn.Sequential(
    OrderedDict([
        ('conv1', nn.Conv2d(3, 3, 3)),
        ('bn1', nn.BatchNorm2d(3)),
        ('relu1', nn.ReLU())
    ])
)
print('net1', net1)
print('net2', net2)
print('net3', net3)
print('可以根据名字或者序号取出子module')
print(net1.conv, '\n', net2[0])
print('#' * 100)
input = V(t.rand(1, 3, 4, 4))
output = net1(input)
output = net2(input)
output = net3(input)
output = net3.relu1(net1.batchnorm(net1.conv(input)))
modellist = nn.ModuleList([
    nn.Linear(3, 4),
    nn.ReLU(),
    nn.Linear(4, 2)
])
input = V(t.randn(1, 3))
for model in modellist:
    input = model(input)

print('当modulelist没有实现forward方法，下面会报错：')
try:
    output = modellist(input)
except TypeError as e:
    print('要实现forward方法')
    print(e)


class MyModule(nn.Module):
    def __init__(self):
        super(MyModule, self).__init__()
        # 这个list不会被识别
        self.list = [nn.Linear(3, 4), nn.ReLU()]
        # ModuleList会被识别
        self.module_list = nn.ModuleList([nn.Conv2d(3, 3, 3), nn.ReLU()])

    def forward(self):
        pass


module = MyModule()
print(module)
