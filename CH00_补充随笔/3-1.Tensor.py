# -*- coding: utf-8 -*-
# @TIME : 2021/3/19 12:25
# @AUTHOR : Xu Bai
# @FILE : 3-1.Tensor.py
# @DESCRIPTION :
from __future__ import print_function  # 通过 __future\ 导入新版本某些模块，测试新版本的新功能，等测试成功后再升级到新的版本上.

import torch as t

print('从接口的角度来说，对tensor的操作可分为两类：\n'
      'torch.function,如torch.save等\n'
      'tensor.function,如tensor.view等')
print('为了方便使用，对tensor的操作通常同时支持这两类接口，如torch.sum(a,b)和a.sum(b)功能相同')
print('_' * 100)
print('创建几个Tensor：')
print('根据shape生成')
a = t.Tensor(2, 3)
print(a)
print('list -> tensor')
b = t.Tensor([[1, 2, 3], [4, 5, 6]])
print(b)
print('tensor -> list')
print(b.tolist())
print('torch.size()返回torch.Size对象，它是tuple的子类，但是用起来略有区别等价于tensor.shape')
b_size = b.size()
print(b_size)
print(b.numel())  # 返回b的元素个数
print(b.nelement())  # 与上面等价
print('创建一个和b形状一样的tensor')
c = t.Tensor(b.size())
print(c)
print('创建一个元素为2和3的tensor，注意传入的是一个元组(2,3)，而不是指定形状的2,3')
d = t.Tensor((2, 3))
print(d)
print('补充：')
print(t.ones(2, 3))
print(t.zeros(2, 3))
print(t.arange(1, 6, 3))  # 从1~6步长为3
print(t.linspace(1, 10, 3))  # start (float) - 区间的起始点
# end (float) - 区间的终点#
# steps (int) - 在start和end间生成的样本数#
# out (Tensor, optional) - 结果张量
print('_' * 100)
print(t.randn(2, 3))  # 从标准正态分布（均值为0，方差为1，即高斯白噪声）中抽取的一组随机数
print(t.rand(2, 3))  # 包含了从区间[0, 1)的均匀分布中抽取的一组随机数
print(t.randperm(5))  # 长度为5的随机排列
print(t.eye(2, 3))
print('-' * 50, '常用Tensor操作', '_' * 50)
print('通过tensor.view可以调整tensor的形状，但必须保证前后元素总数一致。view不会修改自身的数据\n'
      '返回的新tensor和源tensor共享内存\n'
      '在实际使用时经常需要添加或者减少某一维度，这时squeeze和unsqueeze就派上了用场')
a = t.arange(0, 6)
print(a)
print(a.view(2, 3))
b = a.view(-1, 3)
print(b)
print('-----------')
# print(b.unsqueeze(1)) # 在第一维上增加1，第几个中括号就表示第几维？
print(b.unsqueeze(-2))
c = b.view(1, 1, 1, 2, 3)
print(c)
print(c.squeeze(0))  # 压缩第0维的“1”
print(c.squeeze())  # 把所有维度维“1”的压缩
a[1] = 100
print(b)  # a和b共享内存，一起改变
print('-' * 50)
print('resize是另一种可以用来调整size的方法，但与view不同，他可以修改tensor的尺寸。\n'
      '如果新尺寸超过了原尺寸，则自动分配新的空间'
      '如果新尺寸小于原尺寸，则之前的数据依旧会被保存')
print(b)

print(b.resize_(1, 3))
print(b.resize_(3, 3))
print('#' * 50, '索引操作', '#' * 50)
a = t.randn(3, 4)
print(a)
print(a[0])
print(a[:, 0])
print(a[0][2] == a[0, 2])  # 两种写法等价
print(a[:2, ])  # 前两行
print(a[:2, :2])  # 前两行的前两列
print(a > 1)  # 返回一个ByteTensor
print(a[a > 1])  # 等价于a.masked_select(a>1) 选择加过与源Tensor不共享空间
print(a[t.LongTensor([0, 1])])  # 第0行和第1行
print('#' * 50, '常见的选择函数', '#' * 50)
print('index_select(input,dim,index): ', '在指定维度dim上选取，例如选取某些行、某些列')
print('masked_select(input, mask): ', '例子如上，a[a>0]，使用ByteTensor进行选取')
print('non_zero(input,dim,index):', '非0元素的下标')
print('gather(input,dim,index):', '根据index，在dim维度上选取数据，输出的size与index一样')
a = t.arange(0, 16).view(4, 4)
print(a)
print('选取对角线的元素')
index = t.LongTensor([[0, 1, 2, 3]])
print(index)
print(a.gather(0, index))
print('选取反对角线的元素')
index = t.LongTensor([[3, 2, 1, 0]]).t()
print(a.gather(1, index))
print('与gather相反的逆操作是scatter_，gather是数据从input中按index取出来，而scatter_是把取出来的数据再放回去')
print('#' * 50, '高级索引', '#' * 50)
print('高级索引可以看作普通索引的扩展，但是高级索引的结果一般不和原始的Tensor共享内存')
x = t.arange(0, 27).view(3, 3, 3)
print(x)
print(x[[1, 2], [1, 2], [2, 0]])
print(x[1, 1, 2], x[2, 2, 0])
print(x[[0, 2], ...])  # x[0]和x[2]
print('#' * 50, 'Tensor类型与转换', '#' * 50)

a = t.Tensor(5, 3)
print(a)
b = a.float()
print(b)
print(a.int())
print(a.type_as(b))
print(a.new(2, 3))  # 按照a的类型新建一个Tensor
print('#' * 50, '逐元素操作', '#' * 50)
print('常用的逐元素操作：abs/sqrt/div/.../cos/ceil/clamp(input,min,max)/sigmoid/trunc(取整)/...')
print('其中clamp:当元素小于min时取min，大于max时取max：截断')
print('#' * 50, '归并操作', '#' * 50)
print('归并操作会使输出形状小于输入，也可以沿着某一维度执行操作。如sum')
print('_' * 50)
print('假设输入的形状是(m, n,k)，有一个简单的记忆方式')
print('如果指定dim=0，输出的形状就是(1,n,k)或者(n,k)')
print('如果指定dim=1，输出的形状就是(m,1,k)或者(m,k)')
print('如果指定dim=2，输出的形状就是(m,n,1)或者(m,n)')
print('size中是否有1，取决于参数keep_dim=True会保留维度1')
print('_' * 50)
b = t.ones(2, 3)
print(b)
print(b.sum(0, keepdim=True))
print('不过cumsum是例外：')
a = t.arange(0, 6).view(2, 3)
print(a)
print(a.cumsum(dim=1))  # 沿着行累加
print('#' * 50, '比较', '#' * 50)
print('gt/lt/ge/le/eq/ne/: 大于/小于/大于等于/小于等于/等于/不等')
print('topk: 最大的k个数')
print('sort：排序')
print('max/min: 比较两个tensor的最大值和最小值')
print('max的三种用法：t.max(tensor),t.max(tensor,dim),t.max(tensor1,tensor2)')
print('#' * 50, '线性代数', '#' * 50)
print('常用的线性代数函数')
print('trace      对角元素之和（矩阵的迹）')
print('diag       对角线元素')
print('triu/tril  上三角/下三角，可指定偏移量')
print('mm/bmm     矩阵乘法，batch的矩阵乘法')
print('addmm/addbmm/addmv     矩阵运算')
print('dot/cross        内积/外积')
print('inverse          求逆矩阵')
print('svd              奇异值分解')
print('--'*50)