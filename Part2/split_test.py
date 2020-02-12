#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 11:44
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : split_test.py
# @Software: PyCharm
s = 'www.github.com is a good site'
# 使用空白字符进行切割
print(s.split())
# 只分割前两个字符
print(s.split(None, 2))
# 使用.进行分割
print(s.split('.'))
myList = s.split()
# 使用/作为分隔符，将myList连接成字符串
print('/'.join(myList))
# 使用,作为分隔符，将myList连接成字符串
print(','.join(myList))