#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 14:34
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : list_test.py
# @Software: PyCharm
a_tuple = ('hello', 666, 'world')
a_list = list(a_tuple)
print(a_list)
# 创建区间对象
a_range = range(1, 5)
print(a_range)
# 将区间转换为列表
b_list = list(a_range)
c_list = list(range(4, 20, 3))
print(b_list)
print(c_list)
