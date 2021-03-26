# -*- coding: utf-8 -*-
# @TIME : 2021/3/26 19:58
# @AUTHOR : Xu Bai
# @FILE :
# @DESCRIPTION :
class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))


x = Gizmo()
try:
    y * Gizmo() * 10
except:
    print('error')
