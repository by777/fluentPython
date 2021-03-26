# -*- coding: utf-8 -*-
# @TIME : 2021/3/26 19:58
# @AUTHOR : Xu Bai
# @FILE :
# @DESCRIPTION :
charles = {
    'name': 'Charles L.Dodgson',
    'born': 1832
}
lewis = charles
print(lewis is charles)
print(id(lewis), id(charles))
lewis['balance'] = 1000
print(charles)
print('可以看出两者是同一个对象的引用，id也印证了这一点')

print('再次比较：')
alex = {
    'name': 'Charles L.Dodgson',
    'born': 1832,
    'balance': 1000
}
# 两者虽然相等，但不是同一个示例
# == 比较值的相等，is比较对象的标识
print(alex == charles)  # True
print(alex is charles)  # False
