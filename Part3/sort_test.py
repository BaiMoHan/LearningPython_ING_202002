#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 15:23
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : sort_test.py
# @Software: PyCharm
a_list = [1, 5, 435, 55, 214, 673]
print(a_list)
# 对列表元素排序
a_list.sort()
print(a_list)
b_list = ['python', 'swift', 'ruby', 'go', 'kotlin', 'erlang']
print(b_list.sort())
print(b_list)
# 按字符串长度比较大小
b_list.sort(key=len)
print(b_list)
# 指定反向排序
b_list.sort(key=len, reverse=True)
print(b_list)
# 只能在python 2中使用的
# def len_cmp(x,y)
#     return 1 if len(x)>len(y) else -1 if len(x)<len(y) else 0
# b_list.sort(len_cmp())
# print(b_list)