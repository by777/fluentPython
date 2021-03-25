# -*- coding: utf-8 -*-
# @TIME : 2021/3/11 10:44
# @AUTHOR : Xu Bai
# @FILE : 5-5.计算阶乘列表，map与filter和列表推导比较
# @DESCRIPTION :
def factorial(n):
    '''
    :returns n!
    '''
    return 1 if n < 2 else n * factorial(n - 1)


fact = factorial
print(list(map(fact, range(6))))

print([fact(n) for n in range(6)])

print(list(map(factorial, filter(lambda n: n % 2, range(6)))))  # 使用map和filter计算直到5！的阶乘

print([factorial(n) for n in range(6) if n % 2])  # 在py3中，map和filter返回生成器，最接近的替代品是列表推导
