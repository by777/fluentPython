# -*- encoding: utf-8 -*-
# @Time : 20/09/27 09:27 
# @Author : Xu Bai
# @File : 2-3.用列表推导和map&filter组合来创建同样的表单.py
# @Desc :
symbols = '$u₣₢₰₱￠￡u¥£$€¢₢₨₨₭￡₣￠₮₦₱'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 1000]
print(beyond_ascii)
beyond_ascii = list(filter(lambda c: c > 1000, map(ord, symbols)))
print(beyond_ascii)
