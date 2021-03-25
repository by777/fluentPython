# -*- coding: utf-8 -*-
# @TIME : 2021/3/24 20:19
# @AUTHOR : Xu Bai
# @FILE : 4-2-1.图像相关层.py
# @DESCRIPTION :
import torch as t
from PIL import Image
from torch.autograd import Variable as V
from torchvision.transforms import ToTensor, ToPILImage

to_tensor = ToTensor()
to_pil = ToPILImage()
lena = Image.open('lena.png')
print(lena.size)
# lena.show()

# 输入是一个batch，batch_size=1
input = to_tensor(lena).unsqueeze(0)  # 在第0维增加一个维度
# 锐化卷积核
kernel1 = t.ones(3, 3) / -9
kernel1[1][1] = 1
conv = t.nn.Conv2d(1, 1, (3, 3), 1, bias=False)
conv.weight.data = kernel1.view(1, 1, 3, 3)
out = conv(V(input))
to_pil(out.data.squeeze(0))

pool = t.nn.AvgPool2d(2, 2)
print(list(pool.parameters()))
out = pool(V(input))
to_pil(out.data.squeeze(0)).show()

# 输入batch_size=2,维度3#
input = V(t.randn(2, 3))
linear = t.nn.Linear(3, 4)
h = linear(input)
print(h)

# 4 channel,初始化标准差为4，0 均值
bn = t.nn.BatchNorm1d(4)
bn.weight.data = t.ones(4) * 4
bn.bias.data = t.zeros(4)

bn_out = bn(h)
print(bn_out.mean(0), bn_out.var(0, unbiased=False))  # 无偏方差
dropout = t.nn.Dropout(0.5)  # .5的概率舍弃
o = dropout(bn_out)
print(o)
