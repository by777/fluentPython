# -*- coding: utf-8 -*-
# @TIME : 2021/3/26 19:58
# @AUTHOR : Xu Bai
# @FILE :
# @DESCRIPTION :

def f(a, b):
    a += b
    return a


x = 1
y = 3
print(f(x, y))

print('列表可变')
a = [1, 2, 3, 4]
b = [5, 6]
print(f(a, b))
print(a)

print('元组不可变')
t = (10, 20)
u = (30, 40)
print(f(t, u))
print(t)
