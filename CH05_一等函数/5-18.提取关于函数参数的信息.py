# -*- coding: utf-8 -*-
# @TIME : 2021/3/11 16:21
# @AUTHOR : Xu Bai
# @FILE : 5-18.提取关于函数参数的信息
# @DESCRIPTION :
from clip import clip

print(clip.__defaults__)
print(clip.__code__)
print(clip.__code__.co_varnames)
print(clip.__code__.co_argcount)
