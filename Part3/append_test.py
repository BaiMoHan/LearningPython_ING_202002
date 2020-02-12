#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 14:44
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : append_test.py
# @Software: PyCharm
a_list = ['github', 666, 999]
a_list.append('good')   # 追加元素
print(a_list)
a_tuple = (3.4, 5.60)
# 追加元组，把元组当成一个元素
a_list.append(a_tuple)
print(a_list)
# 追加列表，把列表当成一个元素
a_list.append([2, 663])
print(a_list)
# 追加元组中的所有元素
a_list.extend(a_tuple)
print(a_list)
# 追加列表中的所有元素
a_list.extend([2, 9964])
print(a_list)
# 追加区间中的所有元素
a_list.extend(range(1, 6))
print(a_list)
# 设置插入位置
a_list.insert(3, a_tuple)
print(a_list)