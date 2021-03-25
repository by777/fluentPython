# -*- encoding: utf-8 -*-
# @Time : 20/09/26 22:24 
# @Author : Xu Bai
# @File : 1-2.一个简单的二维向量类.py 
# @Desc :

from math import hypot


# hypot() 返回欧几里德范数 sqrt(x*x + y*y)


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):  # doctest:
        # __repr__用于把一个对象用字符串的形式表示出来用来辨认
        # __repr__和__str__的区别：
        # 后者在str()和print()函数时才调用，__repr__相比于__str__函数更好，
        # 因为当__str__不存在时，解释器会用__repr__来代替
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):  # 自定义的布尔值，默认情况下，自定义的类常被认为是TRUE的
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1 + v2)
v = Vector(3, 4)
print(abs(v))
print(v * 3)
print(abs(v * 3))
