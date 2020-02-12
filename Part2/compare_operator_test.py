#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 12:28
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : compare_operator_test.py
# @Software: PyCharm

print('5是否大于4', 5 > 4)
print('3的4次方是否大于等90', 3 ** 4 > 90)
print('20是否大于等于20.0', 20 >= 20.0)
import time
# 获取当前时间
a = time.gmtime()
b = time.gmtime()
print(a == b)
print(a is b)   # a与b是两个不同的对象
# is通过id()函数来计算两个对象的地址
print(id(a))
print(id(b))