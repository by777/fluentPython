# encoding: utf-8
# @Time : 20/09/21 12:23
# @Author : Xu Bai
# @File : 1-1.一摞有序的纸牌.py
# @Desc :
import collections
from random import choice

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
print(beer_card)
deck = FrenchDeck()
print(len(deck))
print(deck[0])
print(deck[-1])
print('------------')
print(choice(deck))
print(choice(deck))

for card in reversed(deck):  # doctest: +ELLIPSIS
    print(card)
    '''
    Card(rank='A', suit='hearts')
    '''
# 如果类没有实现__contains__()方法，那么in运算符就会顺序迭代

print(Card('Q', 'hearts') in deck)

# 排序
print('排序')
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    # 2最小 A最大 黑桃》红桃》方块》梅花
    rank_value = FrenchDeck.ranks.index(card.rank)
    # print(rank_value)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)
