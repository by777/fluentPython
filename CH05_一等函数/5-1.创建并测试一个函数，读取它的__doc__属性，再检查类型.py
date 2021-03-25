# -*- coding: utf-8 -*-
# @TIME : 2021/3/11 10:25
# @AUTHOR : Xu Bai
# @FILE : 5-1.创建并测试一个函数，读取它的__doc__属性，再检查类型
# @DESCRIPTION :
def factorial(n):
    '''
    :returns n!
    '''
    return 1 if n < 2 else n * factorial(n - 1)


print(factorial(42))
print(factorial.__doc__)
print(type(factorial))
