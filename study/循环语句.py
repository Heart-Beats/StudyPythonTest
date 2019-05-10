#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 打印倒三角形
# rowsAndCols = int(input('请输入行列数：'))
# for i in range(rowsAndCols):
#     for j in range(rowsAndCols):
#         if i>j:
#             print(' ',end='')
#         else:
#             print('* ',end='')
#     print()

# 打印正三角形
rowsAndCols = int(input('请输入行列数：'))
for i in range(rowsAndCols):
    for j in range(rowsAndCols):
        if i + j <= rowsAndCols - 2:
            print(' ', end='')
        else:
            print('* ', end='')
    print()
