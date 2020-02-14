#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 14:49
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : varargs.py
# @Software: PyCharm
# 定义支持参数收集的函数


def test(a,* books):
    print(books)
    for b in books:
        print(b)
    print(a)


if __name__ == '__main__':
    test(5, 'fluent python', 'first python', 'start with python', 'python cook', 'python')