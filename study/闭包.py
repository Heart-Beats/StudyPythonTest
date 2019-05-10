#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def createCounter():
    countMap = {'sum': 0}

    def counter():
        countMap['sum'] += 1
        return countMap['sum']

    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
