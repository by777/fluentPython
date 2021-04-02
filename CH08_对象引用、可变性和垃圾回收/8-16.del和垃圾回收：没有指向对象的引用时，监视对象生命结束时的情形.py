# -*- coding: utf-8 -*-
# @TIME : 2021/3/26 19:58
# @AUTHOR : Xu Bai
# @FILE :
# @DESCRIPTION :

import weakref

s1 = {1, 2, 3}
s2 = s1


def bye():
    print('Gone with the wind...')


ender = weakref.finalize(s1, bye)
print(ender.alive)
del s1  # del不删除对象，而是删除对象的引用
print(ender.alive)
s2 = 'spam'  # s2指向了别处，s1销毁
print(ender.alive)
