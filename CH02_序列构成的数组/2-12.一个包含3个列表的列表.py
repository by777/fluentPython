# -*- encoding: utf-8 -*-
# @Time : 20/10/18 15:24 
# @Author : Xu Bai
# @File : 2-12.一个包含3个列表的列表.py 
# @Desc :
board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)
