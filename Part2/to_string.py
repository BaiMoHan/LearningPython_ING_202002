#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 15:30
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : to_string.py
# @Software: PyCharm
str1 = "age="
age = 20
print(str1+str(age))    # 使用str()转换成字符串
age = 20
print(age)
print(str1+repr(age))   # 使用repr()转换成字符串
print(repr(str1))       # 输出带引号的字符串
