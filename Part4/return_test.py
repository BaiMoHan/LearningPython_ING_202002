#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 13:43
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : return_test.py
# @Software: PyCharm
def test():
    for i in range(10):
        for j in range(10):
            print('i的值是：%d,j的值是%d' % (i, j))
            if j == 1:
                return
            print('return后的输出语句')


if __name__ == '__main__':
    test()

