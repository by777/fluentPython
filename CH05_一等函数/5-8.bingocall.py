# -*- coding: utf-8 -*-
# @TIME : 2021/3/11 10:54
# @AUTHOR : Xu Bai
# @FILE : 5-8.bingocall
# @DESCRIPTION : 调用BingoCage实例，从打乱的列表中取出一个元素
import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty Bingocage')

    def __call__(self):  # bingo.pick的快捷键是bingo()
        return self.pick()


if __name__ == '__main__':
    bingo = BingoCage(range(3))
    print(bingo.pick())
    print(bingo())
    print(callable(bingo))
    print(callable(bingo.pick()))
    print(callable(bingo.pick))
