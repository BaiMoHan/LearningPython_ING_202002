#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 17:46
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : pass_test.py
# @Software: PyCharm
s = input('请输入一个整数')
s = int(s)
if s > 5:
    print('s>5')
elif s < 5:
    pass
else:
    print('s=5')