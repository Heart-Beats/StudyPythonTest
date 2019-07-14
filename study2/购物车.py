#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Goods:
    def __init__(self, id, goodname, price) -> None:
        self.__id = id
        self.__goodName = goodname
        self.__price = price

    @property
    def id(self):
        return self.__id

    @property
    def goodname(self):
        return self.__goodName

    @property
    def price(self):
        return self.__price

    def __str__(self) -> str:
        return '%d. %s %d' % (self.__id, self.__goodName, self.__price)


class ShoppingCart:
    __shoppingGoods = []

    def addgoods(self, good):
        self.__shoppingGoods.append(good)

    def totalprice(self):
        from functools import reduce
        return reduce(lambda x, y: x + y, map(lambda goods: goods.price, self.__shoppingGoods))

    def goodslist(self):
        return self.__shoppingGoods


Ryzen2700X = Goods(1, 'Ryzen 2700X', 1619)
MSIB450 = Goods(2, 'MSI B450', 800)
Samsung970EVO = Goods(3, 'Samsung 970EVO', 540)
SapphireRX590 = Goods(4, 'Sapphire RX590', 2000)
goodsList = [Ryzen2700X, MSIB450, Samsung970EVO, SapphireRX590]

salary = int(input('请输入你的工资：'))
for goods in goodsList:
    print(goods, end='; ')
print()
salaryBalance = salary
shoppingCart = ShoppingCart()
while salaryBalance:
    goodsId = int(input('请输入购买商品编号：'))
    if goodsId == -1:
        print('退出购买！')
        break
    else:
        inputTag = False
        for goods in goodsList:
            if goodsId == goods.id:
                inputTag = True
                if salaryBalance < goods.price:
                    print('余额不足，无法购买')
                    break
                salaryBalance -= goods.price
                shoppingCart.addgoods(goods)
                print('你购买了%s，余额：%d' % (goods.goodname, salaryBalance))
        if not inputTag:
            print('你输入的商品编号有误！')

print('你购买的商品如下：')
for shopping in shoppingCart.goodslist():
    print(shopping.goodname, shopping.price, end='; ')
print()
print('总价：%s，你的余额：%s' % (shoppingCart.totalprice(), salaryBalance))
