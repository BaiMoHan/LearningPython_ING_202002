#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 13:13
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : continue_test.py
# @Software: PyCharm
for i in range(0, 3):
    print('i的值是：',i)
    if i == 1:
        continue
    print('continue后的输出语句')