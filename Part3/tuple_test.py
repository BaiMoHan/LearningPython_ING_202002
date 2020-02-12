#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 14:42
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : tuple_test.py
# @Software: PyCharm

a_list = ['github', 666, 999]
a_tuple = tuple(a_list)
print(a_tuple)
# 使用range函数创建区间对象
a_range = range(1, 5)
print(a_range)
b_tuple = tuple(a_range)
print(b_tuple)
c_tuple = tuple(range(4, 20, 3))
print(c_tuple)