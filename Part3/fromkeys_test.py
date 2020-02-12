#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 16:27
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : fromkeys_test.py
# @Software: PyCharm
a_dict = dict.fromkeys(['a', 'b'])
print(a_dict)
b_dict = dict.fromkeys((13, 17))
print(b_dict)
# 使用元组创建包含两个key的字典，指定默认的value
c_dict = dict.fromkeys((13, 17), 'good')
print(c_dict)