#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 14:03
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : translate.py
# @Software: PyCharm

# 同时对元组使用加法、乘法
order_endings = ('st', 'nd', 'rd')\
    +('th',) * 17 + ('st', 'nd', 'rd')\
    +('th',) * 7 +('st',)
print(order_endings)
day = input("输入日期（1-31）：")
day_int = int(day)
print(day + order_endings[day_int-1])