# -*- coding: utf-8 -*-
# @TIME : 2021/3/11 15:56
# @AUTHOR : Xu Bai
# @FILE : 5-12.
# @DESCRIPTION : bobo -f hello.py then curl -i http://localhost:8080/?person=Jim
import bobo


@bobo.query('/')
def hello(person):
    return 'Hello %s !' % person
