#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class People(object):
    __slots__ = ('name', 'age')
    pass


class Student(People):
    __slots__ = ('score')
    pass


nick = Student()
nick.age = 24
print(nick.age)
