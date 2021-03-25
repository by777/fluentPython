# -*- coding: utf-8 -*-
# @TIME : 2021/3/11 11:17
# @AUTHOR : Xu Bai
# @FILE : 列出常规对象没有而函数有的属性
# @DESCRIPTION :
class C: pass


def func(): pass


obj = C
print('func: ')
print(sorted(set(dir(func))))

print('obj: ')
print(sorted(set(dir(obj))))

print('---------------')
print(sorted(set(dir(func)) - set(dir(obj))))
