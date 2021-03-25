# -*- coding: utf-8 -*-
# @TIME : 2021/3/10 20:39
# @AUTHOR : Xu Bai
# @FILE : 4-6.处理UnicodeEncodeError
# @DESCRIPTION :
# 多数非UTF编码器只能处理Unicode的一小部分子集。把文本转换成字节序列时，如果目标编码中没有定义某个字符，
# 那就会抛出UnicodeEncodeError异常，除非把errors参数传给编码方法或函数，对错误进行特殊处理，处理方式如下：

city = 'São Paulo'
print(city.encode('utf_8'))  # utf_?编码能处理任何字符串

print(city.encode('utf_16'))

print(city.encode('iso8859_1'))

try:
    print(city.encode('cp437'))
except UnicodeEncodeError as e:
    print(e)

print(city.encode('cp437', errors='ignore'))
print(city.encode('cp437', errors='replace'))
print(city.encode('cp437', errors='xmlcharrefreplace'))
