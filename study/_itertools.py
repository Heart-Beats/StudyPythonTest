#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
from functools import reduce


def pi(N):
    oddnumber = itertools.count(1, 2)
    oddnumberPN = itertools.takewhile(lambda n: n < 2 * N, oddnumber)
    return reduce(lambda x, y: x + y, list(map(oddmap, list(oddnumberPN))))


def oddmap(n):
    if (n // 2) % 2 != 0:
        return -4 / n
    return 4 / n


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
