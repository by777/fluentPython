# -*- coding: utf-8 -*-
# @TIME : 2021/3/23 19:58
# @AUTHOR : Xu Bai
# @FILE :
# @DESCRIPTION :

"""
计算移动平均值的高阶函数，不保存所有历史值，但有缺陷
"""


def make_average():
    count = 0
    total = 0
    series = []

    def averager(new_value):
        series.append(new_value)
        count += 1
        total += new_value
        return total / count

    return averager


avg = make_average()
try:
    avg(10)
except UnboundLocalError as e:
    print('当count是数字或任何不可变类型时，count = count + 1实际上为count赋值了，这会把count'
          '变为局部变量，total也受这个影响'
          'series本身是可变对象，不受这个影响')
    print(e)

print('解决方法')
ef
make_average():
count = 0
total = 0
series = []


def averager(new_value):
    series.append(new_value)
    nonlocal count, total
    # 把变量标记为自由变量，即使在函数中为变量赋予新值了，也会变成自由变量。
    # 如果nonlocal声明的变量赋予新值，闭包中保存的绑定会更新
    count += 1
    total += new_value
    return total / count


return averager
