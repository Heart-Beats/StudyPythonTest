#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0].lower()


L2 = sorted(L, key=by_name)
print(L2)


def by_score(t):
    return -t[1]

L2 = sorted(L, key=by_score)
print(L2)



def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2,f3 =count()
print(f2())