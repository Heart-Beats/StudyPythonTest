#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools
import time


def metric(fn):
    print('%s executed in %s ms' % (fn.__name__, 10.24))
    # @functools.wraps(fn)

    return lambda *args, **kw: fn(*args, **kw)


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功！')


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin call')
        print('call %s():' % func.__name__)
        result = func(*args, **kw)
        print('end call')
        return result

    from types import FunctionType
    if isinstance(func, FunctionType):
        return wrapper
    else:
        text = func

        def decorator(fun):
            print('%s %s():' % (text, fun.__name__))
            nonlocal func
            func = fun
            return wrapper

        return decorator


@log('execute')
def test():
    pass


f = test()
print(test.__name__)
