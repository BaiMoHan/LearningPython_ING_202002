#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 11:46
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : for_dict.py
# @Software: PyCharm
my_dict = {'Chinese': 89, 'Math': 100, 'English': 63}
# 通过items（）方法遍历所有的key-value
for key, value in my_dict.items():      # 序列解包的应用
    print('key=', key)
    print('value=', value)
print('---------------------------')
# 通过keys方法遍历所有的key
for key in my_dict.keys():
    print('key=', key)
    # 再通过key获得value
    print('value=', my_dict[key])
print('---------------------------')
# 通过value方法获得所有的value
for value in  my_dict.values():
    print('value=', value)