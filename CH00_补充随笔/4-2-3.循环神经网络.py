# -*- coding: utf-8 -*-
# @TIME : 2021/3/25 11:03
# @AUTHOR : Xu Bai
# @FILE : 4-2-3.循环神经网络.py
# @DESCRIPTION :
import torch as t
from torch import nn
from torch.autograd import Variable as V

t.manual_seed(1000)
print('RNN和RNNCell层的区别在于前者能处理整个序列，而后者只处理序列中一个时间点的数据，前者封装更完备更易于使用，后者更具有灵活性')

# 输入：batch_size=3, 序列长度都为2，序列中每个元素占4维
input = V(t.randn(2, 3, 4))
# lstm输入向量4维，3个隐藏元，1层
lstm = nn.LSTM(4, 3, 1)
# 初始状态:1层，batch_size=3,3个隐藏元
h0 = V(t.randn(1, 3, 3))
c0 = V(t.randn(1, 3, 3))

out, hn = lstm(input, (h0, c0))
print(out)

t.manual_seed(1000)
input = V(t.randn(2, 3, 4))
# 一个LSTMCELL对应的层数只能是1层
lstm = nn.LSTMCell(4, 3)
hx = V(t.randn(3, 3))
cx = V(t.randn(3, 3))
out = []
for i in input:
    hx, cx = lstm(i, (hx, cx))
    out.append(hx)
t.stack(out)

# 词向量在自然语言处理
# 有4个词，每个词用5维的向量表示
embedding = nn.Embedding(4, 5)
# 可以用预训练好的词向量初始化embedding
#####################有错误
# embedding.weight.data = t.arange(0, 20).view(4, 5)s
# input = V(t.arange(3, 0, -1)).long()
# output = embedding(input)
# print(output)
#####################
