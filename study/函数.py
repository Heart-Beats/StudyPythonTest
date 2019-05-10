#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


# 求一元二次方程的解
def quadratic(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print('该方程无实数解')
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2


# 测试
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if set(quadratic(2, 3, 1)) != {-1.0, -0.5}:
    print('测试失败')
elif set(quadratic(1, 3, -4)) != {-4.0, 1.0}:
    print('测试失败')
else:
    print('测试成功')


# 计算多数的乘积
def majorityMultiplication(arg, *args):
    if arg is None:
        raise TypeError
    else:
        sum = arg
        for i in args:
            sum = sum * i
        return sum


# 测试
print('majorityMultiplication(5) =', majorityMultiplication(5))
print('majorityMultiplication(5, 6) =', majorityMultiplication(5, 6))
print('majorityMultiplication(5, 6, 7) =', majorityMultiplication(5, 6, 7))
print('majorityMultiplication(5, 6, 7, 9) =', majorityMultiplication(5, 6, 7, 9))
if majorityMultiplication(5) != 5:
    print('测试失败!')
elif majorityMultiplication(5, 6) != 30:
    print('测试失败!')
elif majorityMultiplication(5, 6, 7) != 210:
    print('测试失败!')
elif majorityMultiplication(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        majorityMultiplication()
        print('测试失败!')
    except TypeError:
        print('测试成功!')


# 阶乘
def fact(n, flag):
    if flag == 0:
        return fact_iter(n, 1)
    elif flag == 1:
        return fact_while(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


def fact_while(num, product):
    while (num > 1):
        product *= num
        num -= 1
    return product

print('5! =', fact(5,0))
print('5! =', fact(5,1))

#汉诺塔
def hanoiTower(n,a,b,c):
    if n == 1:
        print(a,'--->',c)
    else:
        hanoiTower(n-1,a,c,b)
        hanoiTower(1,a,b,c)
        hanoiTower(n-1,b,a,c)

hanoiTower(3,'A','B',"c")