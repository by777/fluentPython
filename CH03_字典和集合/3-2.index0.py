# -*- coding: utf-8 -*-
# @TIME : 2021/1/2 21:19
# @AUTHOR : Xu Bai
# @FILE : index0.py
# @DESCRIPTION :  3-2.用setfault处理找不到的键
'''
创建一个从单词到其出现情况的映射
'''
import sys
import re

WORD_RE = re.compile(r'\w+')

index = {

}

with open(sys.argv[1], encoding='UTF-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            occurrences = index.get(word, []) # 提取word出现的情况，如果还没有它的记录，返回[]
            occurrences.append(location) # 把单词新出现的情况添加到列表的后面
            index[word] = occurrences

# 以字母顺序打印出结果
for word in sorted(index, key=str.upper):
    print(word, index[word])
