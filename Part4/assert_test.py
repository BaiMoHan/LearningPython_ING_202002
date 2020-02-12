#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 17:48
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : assert_test.py
# @Software: PyCharm
s_age = input("请输入您的年龄：")
s_age = int(s_age)
assert 20 < s_age < 80
print("您的年龄在20-80之间")