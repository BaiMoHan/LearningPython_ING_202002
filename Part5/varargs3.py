#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 14:58
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : varargs3.py
# @Software: PyCharm


def test(x, y, z=3, *books, **scores): # **代表收集关键字参数
    print(x, y, z)
    print(books)    # 收集参数保存的是元组
    print(scores)   # 对于关键字参数保存的是字典形式


if __name__ == '__main__':
    test(1, 2, 3, 'fluent phthon', 'first python', Chinese=89, Math=36)
    test(1, 2, Chinese=88, Englishi=88)