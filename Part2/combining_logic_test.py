#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 12:37
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : combining_logic_test.py
# @Software: PyCharm

bookname = 'fluent python'
price = 119
version = 'first'
if bookname.endswith('python') and (price < 50 or version == 'first'):
    print("购买")
else:
    print("不购买")