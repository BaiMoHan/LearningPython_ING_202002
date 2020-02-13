#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 16:25
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : multi_return.py
# @Software: PyCharm


def sum_and_avg(list):
    sum = 0
    count = 0
    for e in list:
        # 如果元素e是数值
        if isinstance(e,int) or isinstance(e, float):
            count += 1
            sum += e
    return sum, sum/count


my_list = [20, 59, 6630.56, 'o', 'git', 'ya', '555']
tp = sum_and_avg(my_list)
print(tp)   # 多个返回值是元组
# 进行序列解包
s, avg = sum_and_avg(my_list)
print(s, avg)