# -*- coding: utf-8 -*-
# @TIME : 2021/1/2 20:05
# @AUTHOR : Xu Bai
# @FILE : 2-22.对ndarray的行列进行基本操作
# @DESCRIPTION :
import numpy as np

a = np.arange(12)
print(type(a))
print(a.shape)
a.shape = 3, 4
print(a)
print(a[2])
print(a[:, 1])
print(a.transpose())
