#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 13:11
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : break_out.py
# @Software: PyCharm
exit_flag = False
for i in range(0,5):
    for j in range(0,3):
        print('i的值为', i, 'j的值为',j)
        if j ==1:
            exit_flag = True
            break
    if exit_flag:
        break
