# -*- coding: utf-8 -*-
# @TIME : 2021/3/30 20:14
# @AUTHOR : Xu Bai
# @FILE : squeezenet.py
# @DESCRIPTION :
from models.basic_module import BasicModule
from torch import nn
from torch.optim import Adam
from torchvision.models import squeezenet1_1


class SqueezeNet(BasicModule):
    def __init__(self, num_classes=2):
        super(SqueezeBet, self).__init__()
        self.model_name = 'squeezenet'
        self.model = squeezenet1_1(pretrained=True)
        # 修改原始的num_class: 预训练模型是1000分类
        self.model.num_classes = num_classes
        self.model.classifier = nn.Sequential(
            nn.Dropout(p=0.5),
            nn.Conv2d(512, num_classes, 1),
            nn.ReLU(inplace=True),
            nn.AvgPool2d(13, stride=1)
        )

    def forward(self, x):
        return self.model(x)

    def get_optimizer(self, lr, weight_decay):
        """
        因为使用了预训练模型，我们只需要训练后面的分类
        :param lr:
        :param weight_decay:
        :return:
        """
        return Adam(self.model.classifier.parameters(), lr, weight_decay=weight_decay)
