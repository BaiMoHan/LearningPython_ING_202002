#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 15:50
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : local_function_test.py
# @Software: PyCharm
def get_math_func(types, n):   # python支持在函数内定义函数为局部函数，局部函数对外隐藏
    # 定义一个计算平方的局部函数
    def square(n):
        return n ** 2
    # 定义一个计算立方的局部函数
    def cub(n):
        return n ** 3
    # 定义一个计算阶乘的局部函数
    def factorial(n):
        result = 1
        for index in range(2, n + 1):
            result *= index
        return result
    # 调用局部函数
    if types == 'square':
        return square(n)
    elif types == 'cub':
        return cub(n)
    else:
        return factorial(n)


if __name__ == '__main__':
    print(get_math_func('square', 3))
    print(get_math_func('cub', 3))
    print('', 3, sep='')
