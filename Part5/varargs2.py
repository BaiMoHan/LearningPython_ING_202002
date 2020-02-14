#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 14:52
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : varargs2.py
# @Software: PyCharm


def test(* books, num):
    print(books)
    for b in books:
        print(b)
    print(num)


if __name__ == '__main__':
    test('fluent python', 'first python', 'start with python', 'python cook', 'python', num=5)
    # 收集参数放在前面，后面的参数赋值形式必须用关键字参数形式 num=