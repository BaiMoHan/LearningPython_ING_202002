#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 16:16
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : items_test.py
# @Software: PyCharm
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
# 获取字典中所有的key-value对，返回一个dict_item对象
item = cars.items()
print(type(item))
print(item)
print(list(item))
print(list(item)[1])
# 获取字典中所有的key，返回一个dict_key对象
kys = cars.keys()
print(type(kys))
print(kys)
print(list(kys))
# 获取字典中所有的value，返回一个dict_value对象
vals = cars.values()
print(vals)
print(list(vals))
print(list(vals)[2])