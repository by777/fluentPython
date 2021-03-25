# -*- coding: utf-8 -*-
# @TIME : 2021/3/23 19:58
# @AUTHOR : Xu Bai
# @FILE :
# @DESCRIPTION :
import time


def clock(func):
    def clocked(*args):  # 定义内部函数，可以接受任意个定位参数
        t0 = time.perf_counter()  # 以秒为单位的时间浮点值
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        # repr(object)
        # 返回对象的字符串形式。
        # 返回的字符串形式可以通过
        # eval()
        # 函数获取到本来的值。
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked
