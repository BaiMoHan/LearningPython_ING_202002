#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 13:55
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : plus_test.py
# @Software: PyCharm
a_tuple = ('now', 'here', 20)
b_tuple = ('hello', 666)
sum_tuple = a_tuple + b_tuple
print(sum_tuple)
print(a_tuple)
print(b_tuple)
print(a_tuple + (20, 'open'))
a_list = [20, 50, 100, 60]
b_list = ['abc', 'hello', 666]
sum_list = a_list + b_list
print(sum_list)
# 列表不能与元组相加