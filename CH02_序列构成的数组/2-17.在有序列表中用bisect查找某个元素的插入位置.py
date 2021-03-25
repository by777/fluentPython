# -*- coding: utf-8 -*-
# @TIME : 2021/1/2 15:23
# @AUTHOR : Xu Bai
# @FILE : 2-17.在有序列表中用bisect查找某个元素的插入位置
# @DESCRIPTION :
'''
bisect(haystack, needle)在haystack(干草垛)里搜索needle(针)的位置，该位置满足的条件是：
把needle插入这个位置之后haystack还能保持升序。也就是说这个函数返回的位置前面的值，都小于或等于needle的值。
其中haystack必须是一个有序的序列。
你可以先用bisect（haystack，needle）查找位置index，再用haystack.insert(index, needle)插入新值，
但你也可以用insort一步到位，且速度更快
'''
import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1: 2d}   {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '   |'  # 利用该位置来算出需要几个分隔符号
        print(ROW_FMT.format(needle, position, offset))


if __name__ == '__main__':
    print(sys.argv)
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)
