# -*- coding: utf-8 -*-
# @TIME : 2021/3/20 20:09
# @AUTHOR : Xu Bai
# @FILE : 3-2-2.计算图.py
# @DESCRIPTION :
import torch as t
from torch.autograd import Variable as V

x = V(t.ones(1))
b = V(t.rand(1), requires_grad=True)
w = V(t.rand(1), requires_grad=True)

y = w * x
z = y + b
print(x.requires_grad, b.requires_grad, w.requires_grad, y.requires_grad)

print(y.grad_fn)
print(z.grad_fn)
print(z.grad_fn.next_functions)
print(z.grad_fn.next_functions[0][0] == y.grad_fn)

z.backward(retain_graph=True)
print(w.grad)
print('计算w的梯度时需要用到x的数值，这些数值在前向传播时会保存成buffer，在计算完梯度后会自动清空，为了能多次反向传播需要'
      '指定retain_graph来保留这些buffer')
