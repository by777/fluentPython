# -*- coding: utf-8 -*-
# @TIME : 2021/3/20 10:34
# @AUTHOR : Xu Bai
# @FILE : 3-3-3.内部结构与持久化向量化.py
# @DESCRIPTION :
print('tensor分为头信息区（Tensor）和存储区（Storage），一般来说一个tensor有与之对应的storage，'
      'storage是在data之上的接口。不同tensor头信息不同，但却有可能使用相同的storage')
import time

import torch as t

a = t.arange(0, 6)
print(a)
print(a.storage())
b = a.view(2, 3)
print(id(b.storage()) == id(a.storage()))
print('持久化：')
t.save(a, 'a.pth')
b = t.load('a.pth')
print('向量化: 在科学计算时应当极力避免python原生的for循环，尽量使用向量化的数值计算')


def for_loop_add(x, y):
    result = []
    for i, j in zip(x, y):
        result.append(i + j)
    return t.Tensor(result)


x = t.zeros(1000)
y = t.zeros(1000)
t0 = time.time()

for i in range(1000):
    for_loop_add(x, y)
t1 = time.time()
print(t1 - t0)
t2 = time.time()
for i in range(1000):
    x + y
t3 = time.time()
print(t3 - t2)
print('#' * 50, '注意：', '#' * 50)
print('大多数t.function都有一个参数out，可以保存在指定的tensor里'
      '\n t.set_num_threads可以设置使用的cpu数目'
      '\n t.set_printoptions可以设置打印tensor的数值精度和格式')
a = t.arange(0, 20000000)
print(a[-1], a[-2])  # 32bit会溢出
b = t.LongTensor()
t.arange(0, 20000000, out=b)
print(b[-1], b[-2])
a = t.randn(2, 3)
print(a)
t.set_printoptions(precision=10)
print(a)
