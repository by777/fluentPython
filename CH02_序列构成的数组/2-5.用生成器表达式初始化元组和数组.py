# -*- encoding: utf-8 -*-
# @Time : 20/09/27 09:41 
# @Author : Xu Bai
# @File : 2-5.用生成器表达式初始化元组和数组.py 
# @Desc :

# 虽然可以用列表推导来初始化元组，但生成器表达式是一个更好的选择，以为它实际上是一个迭代器
import array

symbols = '$u₣₢₰₱￠￡u¥£$€¢₢₨₨₭￡₣￠₮₦₱'
print(tuple(ord(symbol) for symbol in symbols))

arr = array.array('I', (ord(symbol) for symbol in symbols))
print(arr)
