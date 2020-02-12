#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 13:37
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : slice_test.py
# @Software: PyCharm
my_tuple = (2020, 'China', 666, 'hope', 000, 'powerful')
# 切片slice[start:end:step]   [起始:终止:步长]
print(my_tuple[1:3])    # 默认步长为1
print(my_tuple[-3:-1])
print(my_tuple[1:-2])
print(my_tuple[-3:4])
ano_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(ano_tuple[2:8:2])
print(ano_tuple[2:8:3])
print(ano_tuple[2:-2:2])