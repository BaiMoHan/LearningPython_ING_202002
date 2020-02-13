#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 16:41
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : named_param_test.py
# @Software: PyCharm


def girth(width, height):
    print('width=', width)
    print('height=', height)
    return 2 * (width + height)


if __name__ == '__main__':
    print(girth(3.5,4.8))
    print(girth(width=3.5,height=6.8))
    print(girth(height=55.2,width=9.6))
    print(girth(3, height=6))  # 必须将位置参数放在关键字参数之前才能正确调用