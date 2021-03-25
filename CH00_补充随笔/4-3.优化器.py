# -*- coding: utf-8 -*-
# @TIME : 2021/3/25 19:14
# @AUTHOR : Xu Bai
# @FILE : 4-3.优化器.py
# @DESCRIPTION :
import torch as t
from torch import nn
from torch import optim
from torch.autograd import Variable as V


# 所有的优化算法都继承于optim.Optimizer并实现了自己的优化步骤

# LeNet
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 6, 5),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(6, 16, 5),
            nn.ReLU(),
            nn.MaxPool2d(2, 2)
        )
        self.classifier = nn.Sequential(
            nn.Linear(16 * 5 * 5, 120),
            nn.ReLU(),
            nn.Linear(120, 84),
            nn.ReLU(),
            nn.Linear(84, 10)
        )

    def forward(self, x):
        x = self.features(x)
        x = x.view(-1, 16 * 5 * 5)
        x = self.classifier(x)
        return x


net = Net()
optimizer = optim.SGD(params=net.parameters(), lr=1)
optimizer.zero_grad()  # 梯度清零，等价net.zero_rad
input = V(t.randn(1, 3, 32, 32))
output = net(input)
output.backward(output)  # fake backward
optimizer.step()  # 执行优化

# 为不同的子网络设置不同的学习率，在finetune中经常用到
optimizer = optim.SGD([
    {'params': net.features.parameters()},  # 学习率为1e-4
    {'params': net.classifier.parameters(), 'lr': 1e-1}
], lr=1e-5)

# 只为两个全连接层设置较大的学习率
special_layers = nn.ModuleList([
    net.classifier[0], net.classifier[3]
])
special_layers_params = list(
    map(
        id, special_layers.parameters()
    )
)
base_params = filter(lambda p: id(p) not in special_layers_params, net.parameters())
optimizer = t.optim.SGD([
    {
        'params': base_params
    },
    {
        'params': special_layers.parameters(),
        'lr': .01
    }
], lr=.001)
old_lr = .1
optimizer = optim.SGD([
    {
        'params': net.features.parameters()
    },
    {
        'params': net.classifier.parameters(),
        'lr': old_lr * .1
    }
], lr=1e-5)
