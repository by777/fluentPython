# -*- encoding: utf-8 -*-
# @Time : 20/09/27 09:22 
# @Author : Xu Bai
# @File : 2-1.把一个字符串变成Unicode码位的列表.py 
# @Desc :
symbols = '$u₣₢₰₱￠￡'
codes = []

for symbol in symbols:
    codes.append(ord(symbol))

print(codes)
