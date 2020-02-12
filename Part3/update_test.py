#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 14:59
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : update_test.py
# @Software: PyCharm

a_list = [2, 4, 'op', 'git', 666]
print(a_list)
# 修改列表元素,重新赋值
a_list[2] = 6
print(a_list)
a_list[-2] = 999
print(a_list)
a_list[1:3] = ['a', 'b']
print(a_list)
# 插入元素
a_list[2:2] = [3, 9]
print(a_list)
# 赋值为空列表实现删除元素
a_list[2:5] = []
print(a_list)
# python自动拆解字符串
b_list = [4, 6, 8]
print(b_list)
b_list[1:3] = 'hello'
print(b_list)
c_list = a_list + b_list
print(c_list)
c_list[2:9:2] =['a', 'b', 'c', 'd']
# 使用指定步长切片必须保证赋值个数与待赋值元素个数一致
print(c_list)
print(dir(list))