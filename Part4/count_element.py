#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 11:52
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : count_element.py
# @Software: PyCharm
src_list = [12, 34, 12, 45, 56, 32, 536,45, 45, 546, 324, 234]
statistic = {}
for ele in  src_list:
    if ele in statistic:
        statistic[ele] += 1
    else:
        statistic[ele] = 1
for ele, count in statistic.items():
    print('%s出现的次数是%s' %(ele, count))