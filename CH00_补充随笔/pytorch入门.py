# -*- coding: utf-8 -*-
# @TIME : 2021/3/16 20:04
# @AUTHOR : Xu Bai
# @FILE : pytorch入门.py
# @DESCRIPTION :
from __future__ import print_function

import torch as t

# 构建 5*3矩阵，只是分配了空间，未初始化
x = t.Tensor(5, 3)
print(x)

# 使用[0,1]均匀分布随机初始化二维数组
x = t.rand(5, 3)
print(x)
print(x.size())

# 三种加法
print('-' * 20)
y = t.rand(5, 3)
print(x + y)
print(t.add(x, y))
# 第三种：指定加法结果的输出目标为result
result = t.Tensor(5, 3)
t.add(x, y, out=result)
print(result)

print("-" * 30)
print('最初y：')
print(y)
print('第一种加法，y的结果：不改变y的内容')
y.add(x)
print(y)
print('第二种加法，y的结果：inplace加法，y改变了')
y.add_(x)
print(y)

print('#' * 15 + '注意：函数名字后带下划线_的函数会修改Tensor本身。'
                 '但x.add()会返回一个新的Tensor，而x不变' + '#' * 15)

print('Tensor的选取与numpy类似：')
print(x)
print(x[:, 1])

print('-' * 20)
print('Tensor和numpy的互操作非常容易而且快速。Tensor不支持的操作可以先转为numpy数组，之后再转为Tensor')
x = t.ones(5)
print(x)
b = x.numpy()  # Tensor -> numpy
print(b)

import numpy as np

a = np.ones(5)
print(a)
b = t.from_numpy(a)  # numpy -> Tensor
print(b)
print('#' * 10)

print('在不支持Cuda的机器侠，下一步不会执行')
print(t.cuda.is_available())
if t.cuda.is_available():
    x = x.cuda()
    y = y.cuda()
    print(x + y)
