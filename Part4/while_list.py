#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 18:03
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : while_list.py
# @Software: PyCharm
arc_list = [12, 34, 56, 35, 13, 43, 764, 108]
a_list = []
b_list = []
c_list = []
print(arc_list)
while len(arc_list) > 0:
    # 弹出arc_list的最后一个元素
    ele = arc_list.pop()
    if ele % 3 == 0:
        a_list.append(ele)
    elif ele % 3 == 1:
        b_list.append(ele)
    else:
        c_list.append(ele)
print('整除3:', a_list)
print('整除3余1:', b_list)
print('整除3余2:', c_list)