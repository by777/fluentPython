# -*- coding: utf-8 -*-
# @TIME : 2021/3/25 20:09
# @AUTHOR : Xu Bai
# @FILE : 5.Pytorch中常用的工具.py
# @DESCRIPTION :
import os

import numpy as np
import torch as t
from PIL import Image
from torch.utils import data
from torchvision import transforms as T


class DogCat(data.Dataset):
    def __init__(self, root):
        imgs = os.listdir(root)
        self.imgs = [os.path.join(root, img) for img in imgs]
        # print(self.imgs)

    def __getitem__(self, index):
        # 开始真正读图片
        img_path = self.imgs[index]
        # print(img_path)
        # dog -> 1, cat -> 0
        label = 1 if 'dog' in img_path.split('/')[-1] else 0
        pil_img = Image.open(img_path)
        array = np.array(pil_img)
        data = t.from_numpy(array)
        return data, label

    def __len__(self):
        return len(self.imgs)


dataset = DogCat(r'./data/dogcat/')
img, label = dataset[0]
for img, label in dataset:
    print(img.size(), img.float().mean(), label)

print('观察上面的size知道，形状不一，且未归一化，可以使用torchvision工具包进行处理\n'
      '其中transforms模块提供了对PIL Image对象和Tensor对象的常用操作。\n'
      '如：Resize、CenterCrop、RandomCrop、RandomSizedCrop、Pad、ToTensor、\n'
      'Tensor：Normalize、ToPILImage')
print('但是如果要对图片进行多个操作，可以使用Compose将这些操作拼接起来\n'
      '类似Sequential。注意:\n'
      '这些操作定义后是以对象形式存在，真正使用时需要调用它的__call__。\n'
      '例如resize(224,224)，应先trans=Scale((224,224)),然后调用trans(img)')

trans = T.Compose([
    T.Resize((224, 224)),
    T.CenterCrop(224),  # 从图片中心裁剪出224*224
    T.ToTensor(),
    T.Normalize(mean=[.5, .5, .5], std=[.5, .5, .5])
])


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
img, label = dataset[0]
for img, label in dataset:
    print(img.size(), label)
