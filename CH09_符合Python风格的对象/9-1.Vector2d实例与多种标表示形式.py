# -*- coding: utf-8 -*-
# @TIME : 2021/3/26 19:58
# @AUTHOR : Xu Bai
# @FILE :
# @DESCRIPTION :
from vector2d_v0 import Vector2d

v1 = Vector2d(3, 4)
print(v1.x, v1.y)

x, y = v1
print(x, y)

print(v1)

print('...')
print(repr(v1))
# 这里调用eval函数表明repr函数调用vector2d实例得到的是对构造方法的准确描述
v1_clone = eval(repr(v1))

# print会调用str函数
print(v1_clone == v1)

# bytes会调用__bytes__方法，生成实例的二进制形式
octets = bytes(v1)
print(octets)
