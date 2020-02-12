#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 16:22
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : popitem_test.py
# @Software: PyCharm
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
print(cars)
print(cars.popitem())
print(cars)
print(cars.popitem())
k, v = cars.popitem()
print(k, v)