# -*- coding: utf-8 -*-
# @TIME : 2021/1/2 15:12
# @AUTHOR : Xu Bai
# @FILE : 2-14.list.sort方法与sorted
# @DESCRIPTION :
# list.sort会就地排序列表也就是说不会把原列表复制一份，这也是这个方法返回None的原因，提醒你
# 本方法不会新建一个列表，random、shuffle也遵守了这个惯例
# 而sorted（）则相反
fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))
print(fruits)
print(fruits.sort())  # 就地排序且返回None
print(fruits)
print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len))
fruits.sort(reverse=True, key=len)
print(fruits)
