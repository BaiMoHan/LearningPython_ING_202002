#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 16:20
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : chars_test.py
# @Software: PyCharm

st = 'I love China'
print(st[2])
print(st[-4])   # 最后一位为-1
print(st[3:5])  # 输出索引3一直到输出索引4完后结束
print(st[-4:-1])
print(st[5:])
print(st[:-6])
print('very' in st)
print('love' in st)
print(len(st))
print(max(st))
print(min(st))
print(dir(str))
print(help(str.title))
print(st.title())
print(st.lower())
print(st.upper())