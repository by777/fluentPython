# -*- coding: utf-8 -*-
# @TIME : 2021/3/26 12:07
# @AUTHOR : Xu Bai
# @FILE : 5-2.计算机视觉工具包torchvision.py
# @DESCRIPTION :
"""
torchvision包含3部分：
    1.models：经典网络与预训练好的模型
    2.datasets：常用的数据集加载，设计上都是继承torch.utils.data.Dataset
    3.transforms:常用的数据预处理
"""
import os

import torch as t
from PIL import Image
from torch import nn
from torch.utils import data
from torchvision import datasets
from torchvision import models
from torchvision import transforms as T
from torchvision.transforms import ToPILImage
from torchvision.utils import make_grid, save_image

to_pil = ToPILImage()

normalize = T.Normalize(mean=[.4, .4, .4], std=[.2, .2, .2])
trans = T.Compose([
    T.RandomResizedCrop(224),
    T.RandomHorizontalFlip(),
    T.ToTensor(),
    normalize
])
resnet34 = models.resnet34(pretrained=True, num_classes=1000)
# 默认分类改为10分类
resnet34.fc = nn.Linear(512, 10)
dataset = datasets.MNIST('./data/', download=True, train=False, transform=trans)
to_pil(t.randn(3, 64, 64)).show()


class DogCat_2(data.Dataset):
    def __init__(self, root, transforms=None):
        imgs = os.listdir(root)
        self.imgs = [os.path.join(root, img) for img in imgs]
        self.transforms = transforms

    def __getitem__(self, index):
        img_path = self.imgs[index]
        label = 1 if 'dog' in img_path.split('/')[-1] else 0
        data = Image.open(img_path)
        if self.transforms:
            data = self.transforms(data)
        return data, label

    def __len__(self):
        return len(self.imgs)


dataset = DogCat_2('./data/dogcat/', transforms=trans)
print(len(dataset))
dataloader = data.DataLoader(dataset, shuffle=True, batch_size=16)
dataiter = iter(dataloader)
img = make_grid(next(dataiter)[0], 4)  # 拼成4*4网格图片且转3通
to_pil(img).show()
save_image(img, 'a.png')
Image.open('a.png').show()
