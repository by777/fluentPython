# -*- coding: utf-8 -*-
# @TIME : 2021/1/2 20:10
# @AUTHOR : Xu Bai
# @FILE : 2-23.使用双向队列
# @DESCRIPTION :
'''
利用.append()和.pop()方法，我们可以把列表当作栈或者队列（.append+.pop(0)）来使用。但这很耗时。
collections.deque类(双向队列)是一个线程安全，可以快速从两端添加或删除元素的数据类型。
而且如果想要村存放“最近用到的几个元素”，deque也是一个很好的选择。这是因为在新建一个双向队列的时候，
你可以指定这个队列的大小，如果这个队列满员了，还可以从反向删除过期的元素，然后在尾端添加新元素
'''
from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate(3)  # 旋转，最右边n个元素会被移动到队列左边
print(dq)
dq.rotate(-4)
print(dq)
dq.appendleft(-1)
print(dq)
dq.extend([11, 22, 33])  # 在尾部添加，头端3个元素会被删除
print(dq)
dq.extendleft([10, 20, 30, 40])  # 注意是迭代添加的，所以添加后会逆序
print(dq)
