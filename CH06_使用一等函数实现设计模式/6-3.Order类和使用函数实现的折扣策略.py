# -*- coding: utf-8 -*-
# @TIME : 2021/3/16 19:31
# @AUTHOR : Xu Bai
# @FILE : 6-3.Order类和使用函数实现的折扣策略
# @DESCRIPTION :
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # 上下文
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)  # 计算折扣
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f}> due: {:.2f}>'
        return fmt.format(self.total(), self.due())


def fidelity_promo(order):
    """
    为积分1000以上顾客提供5%折扣
    """
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """
    第二个具体策略：单个商品为20个或以上时提供10%折扣
    """
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


def large_order_promo(order):
    """
        第三个具体策略：订单中不同商品达到10个或以上时提供7%折扣
    """
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


if __name__ == '__main__':
    print('使用不同的策略折扣的实例')
    joe = Customer('John Doe', 0)  # joe的积分是0
    ann = Customer('Ann Smith', 1100)
    cart = [
        LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)
    ]
    print(Order(joe, cart, fidelity_promo))
    print(Order(ann, cart, fidelity_promo))

    banana_cart = [LineItem('banana', 30, .5),
                   LineItem('apple', 10, 1.5)]
    print(Order(joe, banana_cart, bulk_item_promo))

    long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
    print(Order(joe, long_order, large_order_promo))
    print(Order(joe, cart, large_order_promo))
