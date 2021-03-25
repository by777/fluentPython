# -*- coding: utf-8 -*-
# @TIME : 2021/1/3 16:16
# @AUTHOR : Xu Bai
# @FILE : 3-5.利用defaultdect实例而不是setdefault方法
# @DESCRIPTION : defaultdict
'''
那么，不像3-4，现在只是单纯的查找取值而不是通过查找插入新值的时候，如何处理找不到的键呢
有时候为了方便起见，就算某个键在映射里不存在，我们也希望通过这个键取值额时候得到一个默认值。
途径1：
通过defaultdict这个类型而不是普通的dict
途径2：
给自己定义一个dict的子类，然后在子类中实现__missing__方法
'''
import sys
import re
import collections

WORD_RE = re.compile(r'\w+')
index = collections.defaultdict(list) # 把list构造方法作为default_factory来创建一个defaultdict
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location)# 如果index没有word的调用，那default_factory会被调用，
            # 为查询不到的键创建一个值，这里是一个空的列表。然后这个空列表呗赋值给index[word]，继而被当作返回值返回，
            # 因此总能append成功
for word in sorted(index, key=str.upper):
    print(word, index[word])