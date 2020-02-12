#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 15:31
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : create_dict.py
# @Software: PyCharm
scores = {'chinese': 90, 'math': 100, 'english': 66}
print(scores)
empty_dict = {}
print(empty_dict)
# 使用元组当key,列表是可变的，所以不允许作为key
dict2 = {(20, 30): 'good', 30: 'bad'}
print(dict2)
vegetable = [('celery', 1.58), ('brocoli', 1.29), ('lettuce', 2.18)]
print(vegetable)
dict3 = dict(vegetable)
print(dict3)
cars = [['BMW', 8.5], ['BENS', 8.3], ['AUDI', 7.9]]
dict4 = dict(cars)
print(dict4)
# 创建一个空字典
dict5 = dict()
print(dict5)
# 使用关键字参数来创建字典
dict6 = dict(spinach=1.39, cabbage=2.59)    # 不需要将字符串放在引号中
print(dict6)
