# -*- coding: utf-8 -*-
# @TIME : 2021/1/2 15:43
# @AUTHOR : Xu Bai
# @FILE : 2-18.根据一个分数，查找它所对应的成绩
# @DESCRIPTION :
import bisect


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    print(i)
    return grades[i]


r = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
print(r)
