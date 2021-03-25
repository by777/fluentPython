# -*- encoding: utf-8 -*-
# @Time : 20/09/27 09:34 
# @Author : Xu Bai
# @File : 2-4.使用列表推导计算笛卡尔积.py 
# @Desc :
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print('这种情况先以颜色排列，再以大小排列')
print(tshirts)
print('---------------------------')
tshirts = [(color, size) for size in sizes for color in colors]
print('这种情况先以大小排列，再以颜色排列')
print(tshirts)
