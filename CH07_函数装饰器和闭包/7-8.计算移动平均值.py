# -*- coding: utf-8 -*-
# @TIME : 2021/3/23 19:58
# @AUTHOR : Xu Bai
# @FILE :
# @DESCRIPTION :
print('方法一：用类实现计算移动平均值')


class Average():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


avg = Average()
print(avg(10))
print(avg(11))
print(avg(12))

print('方法二：使用高阶函数计算高阶函数')


def make_averager():
    """
    调用maker_averager时，返回一个averager函数对象，每次调用averager时，他会添加计算
    :return:
    """
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))
