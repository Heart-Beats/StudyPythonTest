#!/usr/bin/env python3
# -*- coding: utf-8 -*


# 规范英文名
def normalize(name):
    if isinstance(name, str):
        return name[0].upper() + name[1:].lower()


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# 求积
def prod(L):
    from functools import reduce
    return reduce(lambda x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


def str2float(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
              '.': '.'}
    position = [1]

    def fn(x, y):
        offset = position[0] - s.index('.')
        position[0] += 1
        if offset < 0:
            return x * 10 + y
        elif offset > 0:
            return x + y / 10 ** offset
        else:
            return x

    from functools import reduce
    return reduce(fn, map(lambda s: digits[s], s))


print('str2float(\'123.456\') =''', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
