# -*- encoding: utf-8 -*-
# @Time : 20/09/27 22:52 
# @Author : Xu Bai
# @File : 2-9.定义和使用具名元组.py 
# @Desc :
from collections import namedtuple

# 创建一个具名元组需要两个参数，一个是类名，一个是类的各个字段打的名字
# 后者可以是一个由数个字符串组成的可迭代对象，也可以是由空格分隔开的字段名组成的字符串
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.683234, 139.691122))
print(tokyo)
print(tokyo.population)
print(tokyo[1])
print(City._fields)  # fields属性是一个包含这个类所有字段名的元组
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.6133213, 77.22313))
delhi = City._make(delhi_data)  # 用_make()通过接受一个可迭代对象来生成一个这个类的实例，它的作用跟City(*delhi_data)一致
print(delhi)
print(delhi._asdict())
for key, value in delhi._asdict().items():
    print(key + ':', value)
