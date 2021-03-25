# -*- coding: utf-8 -*-
# @TIME : 2021/3/23 19:58
# @AUTHOR : Xu Bai
# @FILE : 7-1.装饰器通常把函数替换成另一个函数.py
# @DESCRIPTION :

promos = []


def promotion(promo_func):
    promos.append(promo_func)
    return promo_func


@promotion
def fidelity(order):
    """
    为积分1000以上的顾客5%折扣
    :param order:
    :return:
    """
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


@promotion
def bulk_item(order):
    """
    单个商品20个以上，10%折扣
    :param order:
    :return:
    """
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount + + item.total() * .1
    return discount


@promotion
def large_order(order):
    """
    订单中的不同商品达到10个以上时7%折
    :param order:
    :return:
    """
    distinct_items = {
        item.product for item in order.cart
    }
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


def best_promo(order):
    return max(promo(order) for promo in promos)
