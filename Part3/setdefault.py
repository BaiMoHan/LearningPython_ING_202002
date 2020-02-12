#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 16:25
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : setdefault.py
# @Software: PyCharm
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
print(cars.setdefault('PORSCHE', 9.2))
print(cars)
print(cars.setdefault('BMW', 4.5))
print(cars)