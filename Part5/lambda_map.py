#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 17:12
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : lambda_map.py
# @Software: PyCharm
# 传入计算平方的 lambda 表达式作为参数
x = map(lambda x : x ** 2, range(8))
print([e for e in x])
y = map(lambda x : x ** 2 if not x % 2 else 0, range(8))
print([e for e in y])