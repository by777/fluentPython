# -*- coding: utf-8 -*-
# @TIME : 2021/3/25 19:11
# @AUTHOR : Xu Bai
# @FILE : 4-2-4.损失函数.py
# @DESCRIPTION :
import torch as t
from torch.autograd import Variable as V

# batch_size=3，2个类别
score = V(t.randn(3, 3))
# 3个样本分别属于1，0，1类，label必须是LongTensor
label = V(t.Tensor([1, 0, 1])).long()
criterion = t.nn.CrossEntropyLoss()
loss = criterion(score, label)
print(loss)
