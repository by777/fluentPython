# -*- coding: utf-8 -*-
# @TIME : 2021/3/10 20:55
# @AUTHOR : Xu Bai
# @FILE : 4-9.一些平台上的编码问题
# @DESCRIPTION :
with open('cafe.txt', 'w', encoding='utf_8') as f:
    f.write('café')

with open('cafe.txt') as f:
    print(f.read())

print('在写入文件时制指定了文件编码，但在读取文件时没有这么做')
