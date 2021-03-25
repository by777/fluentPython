# -*- coding: utf-8 -*-
# @TIME : 2021/1/3 16:33
# @AUTHOR : Xu Bai
# @FILE : 3-6.特殊方法__missing__
# @DESCRIPTION :把查询的int键转化为字符串
'''
所有的映射类型在处理找不到的键时，都会牵扯到__missing__方法。在__getitem__找不到的时候，如果实现了__missing__就会调用它
'''


class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):  # 如果找不到的键本身就是字符串，就抛出KeyError异常
            raise KeyError(key)
        return self[str(key)]  # 如果找不到的键不是字符串，就转变为字符串再查找

    def get(self, key, default=None):
        try:
            return self[key]  # get方法把查找方法用self[key]的形式委托给__getitem__, 这样在宣布查找失败前，还能通过__missing__再给某个键一个机会
        except KeyError:
            return default  # __missing__也查找失败了，可以抛出异常了

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d[2])
print(d['2'])
print(d.get(2))
print(d.get('2'))
print(d.get(1, 'N/A'))
print(2 in d)
print('2' in d)
