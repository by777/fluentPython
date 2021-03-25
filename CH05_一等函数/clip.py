# -*- coding: utf-8 -*-
# @TIME : 2021/3/11 16:12
# @AUTHOR : Xu Bai
# @FILE : 5-15.clip
# @DESCRIPTION : 在指定长度附近截断字符串的函数

def clip(text, max_len=80):
    '''
    在max_lem前面或后面的第一个空格处截断文本
    :param text:
    :param max_len:
    :return:
    '''
    end = None
    print(help(text.rfind))
    print(help(text.rstrip))
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end == None:
        end = len(text)
    return text[:end].rstrip()  # rstrip() 删除 string 字符串末尾的指定字符（默认为空格） # strip()删除头
