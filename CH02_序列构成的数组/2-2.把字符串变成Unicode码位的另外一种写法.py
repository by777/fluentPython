# -*- encoding: utf-8 -*-
# @Time : 20/09/27 09:25 
# @Author : Xu Bai
# @File : 2-2.把字符串变成Unicode码位的另外一种写法.py 
# @Desc :
symbols = '$u₣₢₰₱￠￡'
codes = [ord(symbol) for symbol in symbols]
print(codes)
