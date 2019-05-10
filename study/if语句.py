#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#条件语句

height = float(input('请输入身高（cm）:'))
weight = float(input('请输入体重（kg）:'))
BMI = weight / ((height/100)**2)
print('BMI指数%.1f' % BMI)
if BMI < 18.5:
    print('过轻')
elif 18.5 <= BMI <= 25:
    print('正常')
elif 25 < BMI <= 28:
    print('过重')
elif 28 < BMI <= 32:
    print('肥胖')
elif BMI > 32:
    print('严重肥胖')