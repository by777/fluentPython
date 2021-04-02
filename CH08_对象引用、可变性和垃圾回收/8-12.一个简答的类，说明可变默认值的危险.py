# -*- coding: utf-8 -*-
# @TIME : 2021/3/26 19:58
# @AUTHOR : Xu Bai
# @FILE :
# @DESCRIPTION :

class HauntedBus:
    """
    备受折磨的幽灵汽车
    """

    def __init__(self, passengers=[]):  # 如果没传入passengers参数，使用默认绑定的列表对象，一开始是空列表
        self.passengers = passengers  # 这个赋值语句把self.passengers变成passengers的别名，
        # 而没有传入passengers参数，后者又是默认列表的别名

    def pick(self, name):
        self.passengers.append(name)  # 在self.passengers上调用remove和append时，
        # 修改的其实是默认列表，它是函数对象的一个属性

    def drop(self, name):
        self.passengers.remove(name)


"""
备受折磨的幽灵乘客
"""
bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers)  # ['Alice', 'Bill']
bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers)  # ['Bill', 'Charlie'] 此时没有异常

bus2 = HauntedBus()
print(bus2.passengers)
bus2.pick('Carrie')
print(bus2.passengers)  # ['Carrie']

bus3 = HauntedBus()  # bus3一开始也是空的，所以还是赋值默认的列表
print(bus3.passengers)  # ['Carrie'] 但默认列表不为空！
bus3.pick('Dave')
print(bus2.passengers)  # ['Carrie', 'Dave']! 登上bus2的Dave出出现在bus2里
print(bus2.passengers is bus3.passengers)  # True
print(bus1.passengers)  # ['Bill', 'Charlie']但bus1.passengers是不同的列表

print('#' * 100)
print('问题在于: 没有指定初始乘客的HauntedBus实例会共享同一个乘客列表')
