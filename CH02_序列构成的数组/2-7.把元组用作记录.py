# -*- encoding: utf-8 -*-
# @Time : 20/09/27 09:53 
# @Author : Xu Bai
# @File : 2-7.把元组用作记录.py 
# @Desc :
# 把元组当作记录使用，当元组的元素顺序改变，那么所携带的信息实际上就丢失了
import os

lax_coordinates = (33.9425, -118.408056)  # 洛杉矶国际机场的经纬度
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)  # 东京市的一些信息
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]  # country code, passport_num
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)
for country, _ in traveler_ids:
    print(country)
print('--元组拆包--')
print('*运算符可以将一个可迭代对象拆开作为函数的参数')
print('divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)')
r = divmod(20, 8)
print(r)
t = divmod(20, 8)
print(t)
print('让一个函数以元组的形式返回多个值，t原本是一个元组')
q, r = divmod(*t)
print(q, r)

_, filename = os.path.split('/home/baixu/python/example.py')
print(_)
print(filename)

print('用*处理剩下的元素')
a, b, *rest = range(5)
print(a, b, rest)
a, b, *rest = range(2)
print(a, b, rest)

a, *body, c, d = range(5)
print(a, body, c, d)
