# -*- encoding: utf-8 -*-
# @Time : 20/10/18 15:01 
# @Author : Xu Bai
# @File : 2-11.纯文本文件形式的收据以一行字符串的形式被解析.py 
# @Desc :
s = 'bicycle'
print(s[::3])
print(s[::-1])
print(s[::-3])

invoice = '''
    9............6.....................................40.............52...............55
    1909    Pimoroni PiBrella   $17.50  3 $52.3213
    1213    Pimo2roni PiBre421lla   $17.50  3 $52.3213
    14129    Pim21oroni PiBrella   $17.4150  3 $452.3213
    194219    Pi41moroni PiBrella   $17.42150  3 $52.143213    
    
'''
SKU = slice(0, 6)
print(SKU)
DESCRIPTION = slice(40, 52)
QUANTITY = slice(52, 55)
UNIT_PRICE = slice(40, 52)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
print(line_items)
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

print('-------------给切片赋值-------------')
l = list(range(10))
print(l)
l[2:5] = [20, 30]
print(l)
del l[5:7]
print(l)
l[3::2] = [11, 12]
print(l)
l[2:5] = [100]  # l[2:5] = 100 错误
print(l)
