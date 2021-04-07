# -*- coding: utf-8 -*-
# @TIME : 2021/3/28 16:11
# @AUTHOR : Xu Bai
# @FILE : __init__.py.py
# @DESCRIPTION :

from .alexnet import AlexNet
from .resnet34 import ResNet34
from .squeezenet import SqueezeNet
# 加上这两行就可以在主函数里写from models import AlexNet了
# from torchvision.models import InceptinV3
# from torchvision.models import alexnet as AlexNet
