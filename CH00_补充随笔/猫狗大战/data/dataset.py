# -*- coding: utf-8 -*-
# @TIME : 2021/3/28 16:11
# @AUTHOR : Xu Bai
# @FILE : dataset.py
# @DESCRIPTION :
"""
数据的相关处理
"""
import os

from PIL import Image
from torch.utils import data
from torchvision import transforms as T


class DogCat(data.Dataset):
    def __init__(self, root, transforms=None, train=True, test=False):
        """
        获取所有图片地址，并根据训练、验证、测试集划分数据
        :param root:
        :param transforms:
        :param train:
        :param test:
        """
        self.test = test
        imgs = [os.path.join(root, img) for img in os.listdir(root)]
        if self.test:
            imgs = sorted(imgs, key=lambda x: int(x.split('.')[-2].split('/')[-1]))
        else:
            imgs = sorted(imgs, key=lambda x: int(x.split('.')[-2]))
        imgs_num = len(imgs)

        # 划分训练集、测试集，验证：测试 = 3：7
        if self.test:
            self.imgs = imgs
        elif train:
            self.imgs = imgs[:int(0.7 * imgs_num)]
        else:
            self.imgs = imgs[int(0.7 * imgs_num):]

        if transforms is None:
            # 数据转换操作，测试验证集和训练的数据转换有所区别
            normalize = T.Normalize(
                mean=[.485, .456, .0406],
                std=[.229, .224, .225]
            )
            # 测试集和验证集
            if self.test or not train:
                self.transforms = T.Compose([
                    T.Resize(224),
                    T.CenterCrop(224),
                    T.ToTensor(),
                    normalize
                ])
            # 训练集
            else:
                self.transforms = T.Compose([
                    T.Resize(256),
                    T.RandomResizedCrop(224),
                    T.RandomHorizontalFlip(),
                    T.ToTensor(),
                    normalize
                ])

    def __getitem__(self, index):
        """
        返回一张图片的数据，如果是测试集，没有图片id，如1000.jpg返回1000
        :param indx:
        :return:
        """
        img_path = self.imgs[index]
        if self.test:
            label = int(self.imgs[index].split('.')[-1].split('/')[-1])
        else:
            label = 1 if 'dog' in img_path.split('/')[-1] else 0
        data = Image.open(img_path)
        data = self.transforms(data)
        return data, label

    def __len__(self):
        return len(self.imgs)


if __name__ == '__main__':
    pass
