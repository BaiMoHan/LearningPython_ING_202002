#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 18:13
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : for_list.py
# @Software: PyCharm
src_list = [12, 234, 324, 45, 124, 663, 765, 44, -21, 546, 9.21, 234.324, 'a', 'q']
my_sum = 0
my_count = 0
for ele in src_list:
    # 如果该元素是整数或者浮点数
    if isinstance(ele, int) or isinstance(ele, float):
        print(ele)
        # 累加该元素
        my_sum += ele
        # 数值元素个数自增
        my_count += 1
print('总和：', my_sum)
print('平均数:', my_sum/my_count)