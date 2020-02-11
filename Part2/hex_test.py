#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 15:09
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : hex_test.py
# @Software: PyCharm

# 以0x开头或者0X开头的16进制形式
hex_value1 = 0x13
hex_value2 = 0XaF
print("hex_value1的值为", hex_value1)
print("hex_value2的值为", hex_value2)
# 以0B或者0b开头的8进制形式
bin_value1 = 0b111
print("bin_value1的值为", bin_value1)
bin_value2 = 0B101
print("bin_value2的值为", hex_value2)

# 以0o或者0O开头的8进制
oct_value1 = 0o54
print("oct_value1的值为", oct_value1)
oct_value2 = 0O101
print("oct_value2的值为", oct_value2)

# 为提高数据的可读性，可以在数字之间加下划线
a=100_199_288_990
print(a)