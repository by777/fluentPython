# -*- coding: utf-8 -*-
# @TIME : 2021/3/10 21:00
# @AUTHOR : Xu Bai
# @FILE : 4-10.分析修正4.9中的问题
# @DESCRIPTION :

fp = open('cafe.txt', 'w', encoding='utf_8')
print(fp)

print(fp.write('café'))  # 默认返回写入的Unicode的字节数
fp.close()

import os

print(os.stat('cafe.txt').st_size)  # 报告文件字节

fp2 = open('cafe.txt')
print(fp2)
print(fp2.encoding)
print(fp2.read())

fp3 = open('cafe.txt', encoding='utf-8')
print(fp3)
print(fp3.read())

print('二进制中读取文件，返回的是BufferedReader对象而不是TextIOWrapper对象')
fp4 = open('cafe.txt', 'rb')
print(fp4)
print(fp4.read())
