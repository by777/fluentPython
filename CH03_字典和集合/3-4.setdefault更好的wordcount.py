# -*- coding: utf-8 -*-
# @TIME : 2021/1/3 16:03
# @AUTHOR : Xu Bai
# @FILE : 3-4.setdefault更好的wordcount
# @DESCRIPTION :
import sys
import re

WORD_RE = re.compile(r'\w+')

index = {

}

with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1): # 从1开始
        # print(line_no)
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word,[]).append(location) # 获取单词的出现情况列表，如果单词
            # 不存在，把单词和一个空列表放进映射，然后返回这个空列表
            # 这里效果等价于：
            # if key not in my_dict:
            #     my_dict[key] = []
            # my_dict[key].append(new_value)

for word in sorted(index, key=str.upper):
    print(word, index[word])
