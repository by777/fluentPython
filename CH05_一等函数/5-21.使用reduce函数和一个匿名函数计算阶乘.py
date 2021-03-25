# -*- coding: utf-8 -*-
# @TIME : 2021/3/11 16:51
# @AUTHOR : Xu Bai
# @FILE : 5-21.使用reduce函数和一个匿名函数计算阶乘
# @DESCRIPTION :
from functools import reduce


def fact(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))


print(fact(5))
