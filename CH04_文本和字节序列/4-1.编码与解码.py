# -*- coding: utf-8 -*-
# @TIME : 2021/3/10 16:46
# @AUTHOR : Xu Bai
# @FILE : 4-1.编码与解码
# @DESCRIPTION :
s = 'café'
print(len(s))

b = s.encode('utf8')
print(b)
print(len(b))
print(b.decode('utf8'))
print('\033[1;31m 如何记住.decode()与.encode()的区别：\033[0m')
print('\033[1;31m 把字节序列想成晦涩难懂的机器磁芯转储，把Unicode字符串想成人类可读的文本，\033[0m')
print('\033[1;31m 那么，把字节序列转成人类可读的文本字符串就是解码，而把字符串变成用于存储或传输的字节序列就是编码 \033[0m')
