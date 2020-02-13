#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 16:30
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : recursive.py
# @Software: PyCharm


def fn(n):
    if n == 0:
        return 1
    elif n == 1:
        return 4
    else:
        return 2 * fn(n-1) + fn(n-2)


if __name__ == '__main__':
    print('fn(10)=', fn(10))