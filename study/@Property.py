#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


class Screen(object):

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if isinstance(width, (int, float)):
            self.__width = width
        else:
            raise TypeError('width must be integer or float')

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, height):
        if isinstance(height, (int, float)):
            self.__height = height
        else:
            raise TypeError('height must be integer or float')

    @property
    def resolution(self):
        return self.__width * self.__height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
