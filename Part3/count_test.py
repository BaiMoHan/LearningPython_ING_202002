#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 15:09
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : count_test.py
# @Software: PyCharm

a_list = [2, 30, 10, 2, 20, 2, 'hhl', [2, 20]]
# 计算2出现的次数
print(a_list.count(2))
print(a_list.count(55))
print(a_list.index(2))
# 从索引2开始，找2出现的位置
print(a_list.index(2, 2))
# 在4到7之间找2的位置
print(a_list.index(2, 4, 7))