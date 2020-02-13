#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 12:06
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : nested_loop_test.py
# @Software: PyCharm
# 外层循环
for i in range(0, 5):
    j = 0
    # 内层循环
    while j < 5:
        print('i的值为%s,j的值为%s' %(i, j))
        j += 1