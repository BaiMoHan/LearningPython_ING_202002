#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 18:09
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : for_test.py
# @Software: PyCharm
s_max = input("请输入想计算的阶乘")
mx = int(s_max)
result = 1
for num in range(1,mx+1,1):
    result *= num
print(result)