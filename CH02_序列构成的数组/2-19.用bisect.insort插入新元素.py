# -*- coding: utf-8 -*-
# @TIME : 2021/1/2 19:36
# @AUTHOR : Xu Bai
# @FILE : 2-19.用bisect.insort插入新元素
# @DESCRIPTION :
'''
排序很耗时，因此在得到一个有序序列后，我们最好能保持他的有序，bisect.insort就是为了这个而存在的
'''
import bisect
import random

SIZE = 7
random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    # print(new_item)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)
