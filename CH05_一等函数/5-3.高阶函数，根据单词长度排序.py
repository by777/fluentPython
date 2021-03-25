# -*- coding: utf-8 -*-
# @TIME : 2021/3/11 10:35
# @AUTHOR : Xu Bai
# @FILE : 5-3.高阶函数，根据单词长度排序
# @DESCRIPTION :
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))


def reverse(word):
    return word[::-1]


print(reverse('testing'))

print(sorted(fruits, key=reverse))
