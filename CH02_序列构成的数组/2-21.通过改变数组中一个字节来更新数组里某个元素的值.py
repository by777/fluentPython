# -*- coding: utf-8 -*-
# @TIME : 2021/1/2 19:56
# @AUTHOR : Xu Bai
# @FILE : 2-21.通过改变数组中一个字节来更新数组里某个元素的值
# @DESCRIPTION :
'''
memoryview是一个内置类，能在不复制内容的情况下操作同一个数组的不同切片，在数据结构之间共享内存。
memoryview.cast会把同一块内存的内容打包一个全新的memoryview对象给你
'''

from array import array

numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
memv_oct = memv.cast('B')  # B类型，也就是无符号类型
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)
memv[-1] = 100
print(numbers)
