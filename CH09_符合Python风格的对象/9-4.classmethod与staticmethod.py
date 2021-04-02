# -*- coding: utf-8 -*-
# @TIME : 2021/3/26 19:58
# @AUTHOR : Xu Bai
# @FILE :
# @DESCRIPTION :
"""
classmethod:定义操作类而不是操作实例的方法，
classmethod改变了调用方法的方式，因此类方法的第一个参数是类自身而不是实例
classmethod最常用的用途是定义备选构造方法

staticmethod装饰器也会改变方法的调用形式，但是第一个参数不受特殊的值。
其实静态方法就是普通的函数，知识碰巧在类的定义体中而不是模块层定义

下面对比
"""


class Demo:
    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args


# 无论怎么调用Demo.klassmeth，它的定义一个参数始终是Demo类
print(Demo.klassmeth(11, 12))

# staticmethod行为与普通的函数类似
print(Demo.statmeth('Statemeth'))
