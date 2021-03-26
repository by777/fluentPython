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

print('#' * 100)
print('ImageFolder：假设所有的文件按文件夹保存，每个文件夹下存储同一个类别的图片，文件夹名为类名')
from torchvision.datasets import ImageFolder

dataset = ImageFolder('./data/dogcat_2')
# cat文件夹对应0，dog:1
print(dataset.class_to_idx)
print(dataset.imgs)
# dataset[0][1]：第1维时第几张图，第二维为1返回label
# dataset[0][0]: 为0返回图片数据

# 加上transform
normalize = T.Normalize(mean=[.4, .4, .4], std=[.2, .2, .2])
trans = T.Compose([
    T.RandomResizedCrop(224),
    T.RandomHorizontalFlip(),
    T.ToTensor(),
    normalize
])

dataset = ImageFolder('./data/dogcat_2', transform=trans)
to_img = T.ToPILImage()
# to_img(dataset[0][0]*.2+.4).show()

print('#' * 100)
print('Dataset只负责数据的抽象，一次调用__getitem__只返回一个样本。在训练神经网络时，是对一个batch的数据进行操作\n'
      '同时还需要对数据shuffle和并行加速等，这使用dataLoader来实现')
from torch.utils.data import DataLoader

dataloader = DataLoader(
    dataset, batch_size=3, shuffle=True,
    num_workers=0,  # 线程数
    drop_last=False  # 不足一个batch的数据是否丢弃,
    # collate_fn:如何将多个样本拼接
)
dataiter = iter(dataloader)
imgs, labels = next(dataiter)
print(imgs.size())

print('#' * 100)
print('在数据处理中，有时会出现某个样本损坏无法处理的问题。这时在__getitem__将出现异常，此时最好的方案是把出错样本剔除\n'
      '但若实在无法剔除，则可以返回None对象，然后在Dataloader中实现自定义的collate_fn，将空对象过滤掉。但要注意，\n'
      '此时，dataloader所返回的一个batch的样本数会少于batch_size')


class NewDogCat(DogCat_2):
    def __getitem__(self, index):
        try:
            return super(NewDogCat.self).__getitem__(index)
        except:
            return None, None


from torch.utils.data.dataloader import default_collate


def my_collate_fn(batch):
    """
    batch中每个元素形如(data,label)
    :param batch:
    :return:
    """
    batch = list(filter(lambda x: x[0] is not None, batch))
    return default_collate(batch)  # 用默认方式拼接过滤后的batch数据


dataset = NewDogCat('./data/dogcat_wrong/', transforms=trans)
print(dataset[5])
dataloader = DataLoader(dataset, 2, collate_fn=my_collate_fn, num_workers=1)
