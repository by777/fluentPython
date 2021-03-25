# -*- coding: utf-8 -*-
# @TIME : 2021/1/3 16:50
# @AUTHOR : Xu Bai
# @FILE : 3-7.字典的变种
# @DESCRIPTION :
'''
collections.OrderedDict
在添加键的时候会保持顺序。因此键的迭代顺序总是一致的。OrderedDict.popitem(last=True)默认删除返回字典里最后一个元素

collections.ChainMap

collections.Counter()会给键准备一个整数计数器
'''

from collections import Counter

ct = Counter('abeacadabra')
print(ct)
ct.update('aaaaaazzz')
print(ct)
print(ct.most_common(3))