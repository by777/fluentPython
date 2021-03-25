# -*- coding: utf-8 -*-
# @TIME : 2021/1/2 19:43
# @AUTHOR : Xu Bai
# @FILE : 2-20.一个浮点型数组的创建，存入和读取
# @DESCRIPTION :
'''
要存放1000w个浮点数时，数组array比list高效的多，因为数组在背后存放的不是float对象而是数字的字节表述
不过，从py3.4开始，数组不再支持像list.sort()这样的就地排序了
'''
from array import array
from random import random

floats = array('d', (random() for i in range(10 ** 7)))  # 利用一个可迭代对象（这里是生成器）建立一个双精度浮点数组（d是类型码）
print(floats[-1])
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')  # 空
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10 ** 7)  # 读取出来
fp.close()
print(floats2[-1])
print(floats2 == floats)
print(floats.__contains__(floats2[-1]))  # 判断数组是否含有某个元素
