# -*- coding: utf-8 -*-
# @TIME : 2021/3/26 19:58
# @AUTHOR : Xu Bai
# @FILE :
# @DESCRIPTION :

t1 = (
    1, 2,
    [30, 40]
)

t2 = (
    1, 2,
    [30, 40]
)

print(t1 == t2)
print(id(t1[-1]))
t1[-1].append(99)
print(t1)
print(id(t1[-1]))
print(t1 == t2)
print('可以看出虽然最后一个列表的id相同，但是t1和t2不相同')
