#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 12:42
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : ternary_operator_test.py
# @Software: PyCharm

a = 5
b = 3
st = 'a>b' if a > b else 'a不大于b'
print(st)
st = 'first sentence', 'a大于b' if a > b else 'a不大于b'
print(st)
c = 5
d = 5
# 三目运算符的嵌套
print('c>d') if c > d else print('c<d') if c < d else print('c=d')