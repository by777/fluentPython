# -*- coding: utf-8 -*-
# @TIME : 2021/3/16 19:58
# @AUTHOR : Xu Bai
# @FILE : 7-1.装饰器通常把函数替换成另一个函数.py
# @DESCRIPTION :
"""
python何时执行装饰器
"""
registry = []


def register(func):
    print('runnig registry (%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('runing f1()')


@register
def f2():
    print('running f2()')


@register
def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()
    print('可以看出，装饰器再导入时运行，而被装饰的函数只有在明确调用的时候才运行')


if __name__ == '__main__':
    main()
