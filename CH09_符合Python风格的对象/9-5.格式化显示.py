# -*- coding: utf-8 -*-
# @TIME : 2021/4/1 19:58
# @AUTHOR : Xu Bai
# @FILE :
# @DESCRIPTION :

"""
内置的format()函数和str.format()函数方法把各个类型的格式化方法委托给相应的.__format__(format_spec)方法
format_spec是格式说明符
它是：
    format(my_obj, format_spec)
    str.format()
"""
br1 = 1 / 2.43
print(br1)

o = format(br1, '.4f')
print(o)

o = '1 BRL = {rate:7.3f} USD'.format(rate=br1)
print(o)

# b是2进制，x是16进制
o = format(42, 'b')
print(o)

o = format(2 / 3, '.1%')
print(o)

from datetime import datetime

now = datetime.now()
print(now)
o = format(now, '%H:%M:%S')
print(o)
o = "It's now {:%I:%M %p}".format(now)
print(o)

print('如果类没有定义__format__方法，从object继承的方法会返回str(my_object)。'
      '如果为vector2d类定义了__str__方法，因此可以这样做')

from vector2d_v1 import Vector2d

v1 = Vector2d(3, 4)
print(v1)
print(format(v1))

print('然而如果传入格式说明符,object.__format__方法会抛出TypeError')
try:
    format(v1, '.3f')
except TypeError as e:
    print(e)

print('我们将实现自己的微语言来解决这个问题')


class Vector2d_format(Vector2d):
    def __format__(self, fmt_spec=''):
        components = (format(c, fmt_spec) for c in self)
        return '({}, {})'.format(*components)
