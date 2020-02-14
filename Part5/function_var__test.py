#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 16:23
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : function_var__test.py
# @Software: PyCharm


def power(base, ex):
    result = 1
    for i in range(1, ex + 1):
        result *= base
    return result


def area(width, height):
    return width * height


if __name__ == '__main__':
    # 将power函数赋值给my_fun，则my_fun可被当成my_fun使用
    my_fun = power
    print(my_fun(3, 4))
    my_fun = area
    print(my_fun(3, 4))