# -*- coding: utf-8 -*-
# @TIME : 2021/3/23 19:58
# @AUTHOR : Xu Bai
# @FILE : 7-1.装饰器通常把函数替换成另一个函数.py
# @DESCRIPTION :
"""
一个函数，读取一个局部变量和一个全局变量
"""
import traceback


def f1(a):
    print(a)
    print(b)


try:
    f1(3)
except NameError as e:
    print(e)

print('******一个吃惊的案例：******')
b = 6


def f2(a):
    print(a)
    print(b)
    b = 9


try:
    f2(4)
except UnboundLocalError as e:
    print(e)
print('****对比******')
b = 100


def f3(a):
    print(a)
    global b
    print(b)
    b = 0


f3(10)
print(b)
