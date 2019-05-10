#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 阶乘
def factorial(num):
    s = 1
    if num == 0:
        return s
    else:
        nums = [i + 1 for i in range(num)]
        for i in nums:
            s *= i
        return s


# 杨辉三角队列
def triangles(rows):
    n = 0
    while n < rows:
        # l = []
        # for m in range(n + 1):
        #     value = factorial(n) // (factorial(m) * factorial(n - m))
        #    l.append(value)
        l = [factorial(n) // (factorial(m) * factorial(n - m)) for m in range(n + 1)]
        formatPrintRow(rows, l)
        n += 1


# 格式化打印每一行
def formatPrintRow(cols, l):
    for i in range(cols - len(l)):
        print(' ', end='')
    for value in l:
        print('%d ' % value, end='')
    print()


triangles(6)
