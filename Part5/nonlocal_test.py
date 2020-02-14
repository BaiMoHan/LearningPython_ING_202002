#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 16:06
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : nonlocal_test.py
# @Software: PyCharm


def foo():
    # 局部变量name
    name = 'Linus'

    def bar():
        nonlocal name  # nonlocal 声明访问的是外层函数的局部变量而不是当前局部函数的局部变量
        print(name)
        # 如果没有nonlocal,报错未定义，因为局部函数内的局部变量会屏蔽外层函数的变量
        name = 'Sun'

    bar()
    print(name)


if __name__ == '__main__':
    foo()
