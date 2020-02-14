#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 17:03
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : lambda_test.py
# @Software: PyCharm
def get_math_func(types):
    result = 1
    # 该函数返回的是lambda表达式
    if types == 'square':
        return lambda n : n ** 2
    elif types == 'cub':
        return lambda n : n ** 3
    else:
        return lambda n : (n + 1) * n / 2
    # 规定lambda表达式只能是单行表达
    # lambda [parameter_list] : 单行表达式


if __name__ == '__main__':
    my_func = get_math_func('square')
    print(my_func(5))
    my_func = get_math_func('cub')
    print(my_func(5))
    my_func = get_math_func('')
    print(my_func(5))