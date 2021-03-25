# -*- encoding: utf-8 -*-
# @Time : 20/10/18 15:32 
# @Author : Xu Bai
# @File : 2-13.含有3个指向同一对象的引用的列表是毫无用处的.py 
# @Desc :
weird_board = [['_'] * 3] * 3
print(weird_board)
weird_board[1][2] = 'X'
print(weird_board)
