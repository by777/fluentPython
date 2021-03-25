# -*- coding: utf-8 -*-
# @TIME : 2021/3/25 20:01
# @AUTHOR : Xu Bai
# @FILE : 4-5.初始化策略.py
# @DESCRIPTION :
print('nn.Module参数提供了较为合理的初始化策略'
      '当我们使用Parameter时，自定义初始化尤为重要，因为t.Tensor()可能返回极大值')
from torch.nn import init
import torch as t
from torch import nn

linear = nn.Linear(3, 4)
t.manual_seed(1)
# 等价于linear.weight.data.normal_(0,std)
init.xavier_normal(linear.weight)
# 对模型所有的参数初始化
