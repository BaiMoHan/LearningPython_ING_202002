#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 13:04
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : break_else.py
# @Software: PyCharm
for i in range(0,10):
    print('i的值是', i)
    if i == 2:
        break
    else:
        print('else块:', i)
else:
    print('end of for')