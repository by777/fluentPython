# -*- coding: utf-8 -*-
# @TIME : 2021/3/20 19:35
# @AUTHOR : Xu Bai
# @FILE : 3-2.autograd.py
# @DESCRIPTION :
"""
torch.autograd就是为方便用户使用，专门开发的一套自动求导引擎，能根据输入和前向传播过程自动构建计算图，并执行反向传播
"""
print('#' * 50, '回忆:', '#' * 50,
      '\ndata: 保存variable保存的tensor' \
      '\ngrad: 保存data对应的梯度，grad也是variable而非tensor，它与data的形状一致' \
      '\ngrad_fn: 指向一个Function，记录variable的操作历史，即它是什么操作的输出，用来构建计算图。' \
      '如果某一个变量是用户创建的，则它为样子结点，指向None')
print('variable的构造函数需要传入tensor，同时可选参数\nrequires_grad:是否需要对该variable求导，'
      '\nvolatile:意为挥发，True时构建在该variable上的图都不会被求导，用于推理阶段设计')
print('\nVariable支持大部分tensor支持的操作，但不支持部分inplace操作，因为这些操作会修改tensor自身，\n'
      '而在反向传播中，variable需要缓存原来的tensor来计算梯度'
      '如果想要计算各个variable的梯度，\n只需要调用**根节点variable**的backward方法，autograd会自动沿着计算图反向传播，计算每一个叶子结点的梯度')
print('##' * 50)
import torch as t
from torch.autograd import Variable as V

a = V(t.ones(3, 4), requires_grad=True)
b = V(t.zeros(3, 4))
c = a.add(b)
print(c)
d = c.sum()
print(d)
print(d.backward())
print('注意下面的区别：')
print(c.data.sum(), c.sum())
print(a.grad)
print('虽然没有指定c需要求导，但c的计算依赖于a，会被自动设为True')
print(a.requires_grad, b.requires_grad, c.requires_grad)
print(a.is_leaf, b.is_leaf, c.is_leaf)

print('#' * 50, '自动求导与手动求导的区别：', '#' * 50)


def f(x):
    """
    y = x**2 + e**x
    导函数为2x * e**x + x **2 * e **x
    """
    y = x ** 2 + t.exp(x)
    return y


def gradf(x):
    """
    手动计算导函数
    """
    dx = 2 * x * t.exp(x) + x ** 2 * t.exp(x)
    return dx


x = V(t.randn(3, 4), requires_grad=True)
y = f(x)
#print(y)
y.backward(t.ones(y.size()))

print(x.grad)
print(gradf(x))
