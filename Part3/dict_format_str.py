#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 16:31
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : dict_format_str.py
# @Software: PyCharm
# 在字符串模板中使用key
temp = '今天是%(year)s年，%(month)s月，%(day)s日'
day = {'year': 2020, 'month': 2, 'day': 12}
print(temp % day)