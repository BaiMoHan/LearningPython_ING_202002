#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 12:03
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : for_else.py
# @Software: PyCharm
a_list = [330, 1.4, 50, 'git', -3.5]
for ele in a_list:
    print('元素：', ele)
else:
    print('else块', ele)
    # 访问循环计数器的值,依然等于最后一个元素的值
