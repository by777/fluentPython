# -*- coding: utf-8 -*-
# @TIME : 2021/1/2 20:32
# @AUTHOR : Xu Bai
# @FILE : 3-0.字典和集合
# @DESCRIPTION :
'''
一般来说用户自定义类型的对象都是可散列的，散列值就是他们的id函数的返回值，但对象不能说可变的
'''
tt = (1, 2, (30, 40))
print(hash(tt))
tl = (1, 2, [30, 40])
try:
    print(hash(tl))
except TypeError as e:
    print(e)
tf = (1, 2, frozenset([30, 40]))
print(hash(tf))
print('字典提供了很多构造方法：\n')
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('one', 1), ('two', 2), ('three', 3)])
e = dict({'one': 1, 'three': 3, 'two': 2})
print(a == b == c == d == e)
print('-'*10 + '常见的映射方法' + '-'*10)
print(d.clear())
print(c.__contains__('one'))
print(c.__contains__(1))
print(c.__contains__(('one', 1)))
print(c.items())
print(c.keys())
print(c.values())