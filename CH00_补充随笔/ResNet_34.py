# -*- coding: utf-8 -*-
# @TIME : 2021/3/15 19:12
# @AUTHOR : Xu Bai
# @FILE : ResNet_34.py
# @DESCRIPTION : 用50行代码搭建ResNet

import torch as t
from torch import nn
from torch.nn import functional as F


class ResidualBlock(nn.Module):
    """
    实现子module：Residual Block
    """

    def __init__(self, inchannel, outchannel, stride=1, shortcut=None):
        super(ResidualBlock, self).__init__()
        self.left = nn.Sequential(
            nn.Conv2d(inchannel, outchannel, 3, stride, 1, bias=False),
            nn.BatchNorm2d(outchannel),
            # in_channels, out_channels, kernel_size, stride, padding, dilation, groups, bias, padding_mode
            nn.Conv2d(outchannel, outchannel, 3, 1, 1, bias=False),
            nn.BatchNorm2d(outchannel)
        )
        self.right = shortcut

    def forward(self, x):
        out = self.left(x)
        residual = x if self.right is None else self.right(x)
        out += residual
        return F.relu(out)


class ResNet(nn.Module):
    """
    实现主Module：resnet34
    resnet34包含多个layer，每一个layer又包含多个resdual block，用子module实现residual block，
    用_make_layer函数实现layer
    """

    def __init__(self, num_classess=1000):
        super(ResNet, self).__init__()
        # 前几层图像转换
        self.pre = nn.Sequential(
            nn.Conv2d(3, 64, 7, 2, 3, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(3, 2, 1)
        )

        self.layer1 = self._make_layer(64, 128, 3)
        self.layer2 = self._make_layer(128, 256, 4, stride=2)
        self.layer3 = self._make_layer(256, 512, 6, stride=2)
        self.layer4 = self._make_layer(512, 512, 3, stride=2)

        self.fc = nn.Linear(512, num_classess)

    def _make_layer(self, inchannel, outchannel, block_num, stride=1):
        """
        构建layer，包含多个residual block
        """
        shortcut = nn.Sequential(
            nn.Conv2d(inchannel, outchannel, 1, stride, bias=False),
            nn.BatchNorm2d(outchannel)
        )
        layers = [ResidualBlock(inchannel, outchannel, stride, shortcut)]
        for i in range(1, block_num):
            layers.append(ResidualBlock(outchannel, outchannel))
        return nn.Sequential(*layers)

    def forward(self, x):
        x = self.pre(x)
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)

        x = F.avg_pool2d(x, 7)
        x = x.view(x.size(0), -1)
        return self.fc(x)


if __name__ == '__main__':
    model = ResNet()
    input = t.autograd.variable(t.randn(1, 3, 244, 244))
    o = model(input)
    print(o)
