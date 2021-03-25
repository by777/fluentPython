# -*- coding: utf-8 -*-
# @TIME : 2021/3/19 15:25
# @AUTHOR : Xu Bai
# @FILE : 3-1.Tensor.py
# @DESCRIPTION :
import numpy as np
import torch as t

print('Tensor和numpy共享内存，转换开销很小，numpy的处理更丰富')
a = np.ones([2, 3], dtype=np.float32)
print(a)
b = t.from_numpy(a)
print(b)
a[0, 1] = 100
print(b)
c = b.numpy()
print(c)
print('广播法则：她在快速执行向量化的同时不会占用额外的存储，Numpy的广播法则如下：\n'
      '1. 让所有的输入数组都向其中shape最长的数组看齐，shape不足的部分通过在前面加1补齐\n'
      '2. 两个数组要不在某一个维度长度一致，要不其中一个为1，否则不能计算\n'
      '3. 当输入数组的某个维度的长度为1时，计算时沿此维度复制扩充成一样的形状'
      'Pytorch已经实现了自动广播法则，但是更建议通过unsqueeze或者view、expand或者expand_as来实现\n'
      'unsqueeze或者view： 为数据某一维的形状补1，实现法则1\n'
      'expand或者expand_as: 重复数组实现法则3，该操作不会复制数组，所以不会占用额外的空间')
a = t.ones(3, 2)
b = t.zeros(2, 3, 1)
print('--------自动广播法则：--------')
print('a是2维，b是3维，所以先在较小的a前面补1'
      '即：a.unsqueeze(0) a的形状变为(1,3,2),b的形状是(2,3,1)'
      '接下来：a和b在第1，3维的形状不一致，其中一个为1\n'
      '因此利用广播法则扩展，两个形状都变成了(2,3,2)')
c = a + b
print(c)
print(c.size())
print('--------手动广播法则：--------')
c = a.view(1, 3, 2).expand(2, 3, 2) + b.expand(2, 3, 2)
print(c)
print('或者：')
c = a.unsqueeze(0).expand(2, 3, 2) + b.expand(2, 3, 2)
print(c)
