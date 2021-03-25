# -*- coding: utf-8 -*-
# @TIME : 2021/3/11 10:50
# @AUTHOR : Xu Bai
# @FILE : 5-6.使用reduce和sum计算0~99的和
# @DESCRIPTION :
from functools import reduce
from operator import add

print(reduce(add, range(100)))
print(sum(range(100)))
