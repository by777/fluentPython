# -*- coding: utf-8 -*-
# @TIME : 2021/3/26 19:58
# @AUTHOR : Xu Bai
# @FILE :
# @DESCRIPTION :
"""
默认浅复制
"""
l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)
# 默认浅复制，只复制值内容
print(l1 == l2)
print(l1 is l2)

l1.append(100)
l1[1].remove(55)
print('l1: ', l1)
print('l2: ', l2)

l2[1] += [33, 22]  # 对可变的对象来说，+=就地修改列表，这次修改在l1[1]中也有体现，因为它是l2[1]的别名
l2[1] += (10, 11)  # 对元组来说，+=创建一个新元组
print('l1: ', l1)
print('l2: ', l2)
