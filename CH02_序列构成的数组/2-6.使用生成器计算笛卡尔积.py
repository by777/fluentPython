# -*- encoding: utf-8 -*-
# @Time : 20/09/27 09:50 
# @Author : Xu Bai
# @File : 2-6.使用生成器计算笛卡尔积.py 
# @Desc :
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for thirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(thirt)
