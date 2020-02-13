#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 16:16
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : function_test.py
# @Software: PyCharm


def my_max(x, y):
    z = x if x > y else y
    return z


def say_hi(name):
    print('===正在执行say_hi函数==')
    return name + ',您好！'


a = 6
b = 9
result = my_max(a, b)
print('result=', result)
print(say_hi('孙悟空'))