#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 15:11
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : int_transfer_test.py
# @Software: PyCharm
def swap(a, b):
    a, b = b, a
    print('swap:',a,b)


if __name__ == '__main__':
    a = 3
    b = 4
    swap(a, b)
    print('main:', a, b)