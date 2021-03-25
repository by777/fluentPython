# -*- coding: utf-8 -*-
# @TIME : 2021/3/11 10:29
# @AUTHOR : Xu Bai
# @FILE : 5-2.通过别的名称使用函数，再把函数作为函数传递
# @DESCRIPTION :
def factorial(n):
    '''
    :returns n!
    '''
    return 1 if n < 2 else n * factorial(n - 1)


fact = factorial
print(fact)
print(fact(5))
print('map函数返回一个可迭代对象，里面的元素是把第一个参数（一个函数）应用到第二个参数中各个元素上得到的结果')
print(map(factorial, range(11)))
print(list(map(fact, range(11))))
