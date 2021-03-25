# -*- coding: utf-8 -*-
# @TIME : 2021/3/18 10:29
# @AUTHOR : Xu Bai
# @FILE : 2-2-2.Autograd：自动微分.py
# @DESCRIPTION :
print('autograd.Variable是AutoGrad中的核心类，它简单封装了Tensor，并支持几乎所有Tensor的操作\n'
      'Tensor被封装为Variable后，可以调用它的.backward实现反向传播，自动计算所有梯度')
print('Variable包含三个属性：')
print('①data:保存Variable所包含的Tensor')
print('②grad:保存data对应的梯度，grad也是个Variable而不是Tensor，它和data的形状一样')
print('③grad_fn:指向一个Function对象，这个Function用来反向传播计算输入的梯度')

import torch as t
from torch.autograd import Variable

print('__' * 50)
print('使用Tensor新建一个Variable：')
x = Variable(t.ones(2, 2), requires_grad=True)
print(x)
y = x.sum()
print(y)
print(y.grad_fn)
print('反向传播，计算梯度：')
print(y.backward())
# y = x.sum() = (x[0][0] + x[0][1] + x[1][0] + x[1][1])
print(x.grad)

print('_' * 100)
print('Variable和Tensor具有近乎一致的接口，在实际使用时可以无缝切换')
x = Variable(t.ones(4, 5))
y = t.cos(x)  # 直接cos Variable
x_tensor_cos = t.cos(x.data)  # cos variable.data也可以
print(y)
print(x_tensor_cos)
