#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 14:15
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : seq_packing.py
# @Software: PyCharm

# 序列封包，将多个值赋值个一个值，最后是创建了一个元组
vals = 10, 20, 99, 66
print(vals)
print(type(vals))
print(vals[1])
a_tuple = tuple(range(1, 10, 2))
# 序列解包，元组内元素一一赋值给变量，要求变量个数与元组元素个数一致
a, b, c, d, e = a_tuple
print(a, b, c, d, e)
a_list = ['hello', 'world']
str1, str2 = a_list
print(str1, str2)
x, y, z = 10, 20, 30
print(x, y, z)
x, y, z = z, x, y
print(x, y, z)
# 解包只解部分元素
first, second, *rest = range(10)
print(first)
print(second)
print(rest)
*begin, last = range(10)
print(begin)
print(last)
first, *middle, last = range(10)
print(first)
print(middle)
print(last)



