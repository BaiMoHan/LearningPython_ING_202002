#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 16:57
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : function_return_test.py
# @Software: PyCharm
def get_math_func(types):   # python支持在函数内定义函数为局部函数，局部函数对外隐藏
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
        return square
    elif types == 'cub':
        return cub
    else:
        return factorial


if __name__ == '__main__':
    math_func = get_math_func('cub')    # 程序返回一个嵌套函数
    # print(math_func)    <function get_math_func.<locals>.cub at 0x0000013E3F41C318>
    print(math_func(5))
    math_func = get_math_func('square')
    print(math_func(5))
    math_func = get_math_func('')
    print(math_func(5))