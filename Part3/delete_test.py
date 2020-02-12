#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 14:51
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : delete_test.py
# @Software: PyCharm

a_list = ['github', 'com', 'hello', 666, 996, 2020]
print(a_list)
del a_list[2]   # 删除第3个元素
print(a_list)
del a_list[1:3]
print(a_list)
a_list = ['github', 'com', 'hello', 666, 996, 2020]
del a_list[2:-2:2]
print(a_list)
name = 'Name'
del name
# remove去除第一个找到的元素，找不到就报错
a_list.remove(666)
print(a_list)
# 清空列表
print(a_list.clear())