# -*- coding: utf-8 -*-
# @TIME : 2021/3/16 19:58
# @AUTHOR : Xu Bai
# @FILE : 7-1.装饰器通常把函数替换成另一个函数.py
# @DESCRIPTION :

"""
装饰器的一大特性：能把被装饰的函数替换成其他函数
2.装饰器在加载模块时立即执行
"""


def deco(func):
    def inner():
        print('running inner()')

    return inner


@deco
def target():
    print('running target()')


print(target())
print(target)
