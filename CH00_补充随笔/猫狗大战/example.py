# -*- coding: utf-8 -*-
# @TIME : 2021/3/29 20:52
# @AUTHOR : Xu Bai
# @FILE : example.py
# @DESCRIPTION :
"""
介绍命令行工具fire
"""
import fire


def add(x, y):
    return x + y


def mul(**kwargs):
    a = kwargs['a']
    b = kwargs['b']
    return a * b


if __name__ == '__main__':
    fire.Fire()
"""
    在命令行：
    python example.py add 1 2
    或者
    python example.py mul --a=1 --b=2
    也可以
    python example,py add --x=1 --y=2
"""
