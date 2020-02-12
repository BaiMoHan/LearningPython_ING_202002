#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 16:11
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : get_test.py
# @Software: PyCharm
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
print(cars)
print(cars.get('BMW'))
print(cars.get('math'))
print(cars.get('AUDI'))
cars.update({'BMW': 4.5, 'PORSCHE': 9.3})
print(cars)