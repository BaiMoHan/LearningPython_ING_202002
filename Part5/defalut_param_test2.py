#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 16:49
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : defalut_param_test2.py
# @Software: PyCharm


# 定义一个打印三角形的函数，带默认值的参数必须放在最后面
def print_triangle(char, height=5):
    for i in range(1, height + 1):
        # 先打印一排空格
        for j in range(height - 1):
            print(' ', end='')
        # 再打印一排特殊字符
        for j in range(2 * i - 1):
            print(char, end='')
        print()


if __name__ == '__main__':
    print_triangle('@', 6)
    print_triangle('#', height=8)
    print_triangle(char='&')
