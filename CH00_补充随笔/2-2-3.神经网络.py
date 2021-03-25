# -*- coding: utf-8 -*-
# @TIME : 2021/3/18 10:46
# @AUTHOR : Xu Bai
# @FILE : 2-2-3.神经网络.py
# @DESCRIPTION :
print('torch.nn构建于Autograd之上')
print('nn.Module是nn最重要的类，包含网络各层定义及forward方法')

print('定义网络时，需要继承nn.Module，并实现它的forward方法，把网络中具有科学系参数的层放在构造函数__init__中'
      '如果某一层如ReLU不具有可学习的参数，则既可以放在构造函数里也可以不放')

import torch as t
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable


class Net(nn.Module):
    def __init__(self):
        # nn.Module子类的函数必须在构造函数中执行父类的构造函数
        # 下式等价于nn.Module.__init__(self)
        super(Net, self).__init__()
        # 1 表示输入图片为单通道，6是输出通道数，5表示卷积核5*5
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        # 全连接层（仿射层），y = Wx + b
        # 输入 32 * 32
        # N = (W - F + 2P) / S + 1 经过各层计算得进入fc层的尺寸N
        self.fc1 = nn.Linear(16 * 13 * 13, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        # 卷积 激活 池化
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        # reshape : -1 表示自适应
        x = x.view(x.size()[0], -1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x


net = Net()
print(net)
print('网络的可学习参数通过net.parameters()返回，net.named_parameters可同时返回可学习的参数和名称')
params = list(net.parameters())
print(len(params))
for name, param in net.named_parameters():
    print(name, ':', param.size())

print('__' * 50)
print('forward函数的输入和输出都是Variable，只有Variable才能自动求导，Tensor是没有的，所以在输入时，需要封装Tensor')
input_data = t.rand(1, 1, 64, 64)  # 返回一个张量，包含了从区间[0, 1)的均匀分布中抽取的一组随机数。张量的形状由参数sizes定义。
print(input_data, input_data.size())
out = net(Variable(input_data))
print(out.size())
net.zero_grad()  # 所有参数梯度清零
out.backward(Variable(t.ones(1, 10)))  # 反向传播
print('##################需要注意的是##################')
print('torch.nn只支持mini_batches，不支持一次只输入一个样本，即一次必须是一个batch\n'
      '如果只想输入一个样本，则用input.unsqueeze(0)将batch_size设置为1'
      '例如，nn.Conv2d输入必须是4维的，形如nSamples * nChannels * Height * Width可将nSample设置为1，即1 * nChannels * Height * Width')
print('##' * 20, '测试一个样本的情况', '##' * 20)
one_sample = Variable(t.ones(1, 64, 64)).unsqueeze(0)
out = net(one_sample)
print(out)

print('计算损失')
output = net(Variable(t.randn(1, 1, 64, 64)))
target = Variable(t.arange(0, 10).view(1, 10))  # 这里.view自己加的，避免广播
# https://www.jianshu.com/p/6e190c4adbb8
output = output.to(t.float32)
target = target.to(t.float32)
criterion = nn.MSELoss()
loss = criterion(output, target)
print(loss)
print(loss.grad_fn)
# 运行.backward，观察调用之前和调用之后的grad
net.zero_grad()  # 把net中所有的可学习参数的梯度清零
print('反向传播之前的conv1.bias的梯度')
print(net.conv1.bias.grad)
loss.backward()
print('反向传播之后bias的梯度')
print(net.conv1.bias.grad)

print('优化器')
import torch.optim as optim

optimizer = optim.SGD(net.parameters(), lr=0.01)
# 在训练过程中先将梯度清零
optimizer.zero_grad()
# 计算损失
output = net(Variable(input_data))
loss = criterion(output, target)
# 反向传播
loss.backward()
# 更新参数
optimizer.step()
print(net.conv1.bias.grad)
