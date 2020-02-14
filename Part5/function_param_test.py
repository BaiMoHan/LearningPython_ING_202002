#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 16:45
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : function_param_test.py
# @Software: PyCharm
# 定义函数类型的形参，其中fn是一个函数
def maps(data, fn):
    result = []
    # 遍历data列表中每一个元素，并用fn函数对每个元素进行计算
    # 然后将计算结果作为新数组的元素
    for e in data:
        result.append(fn(e))
    return result


# 定义一个计算平方的函数
def square(n):
    return n ** 2


# 定义一个计算立方的函数
def cub(n):
    return n ** 3


# 定义一个计算阶乘的函数
def factorial(n):
    result = 1
    for index in range(2, n + 1):
        result *= index
    return result


if __name__ == '__main__':
    data = [3, 4, 9, 5, 8]
    print('data=',data)
    print('square=', maps(data, square))
    print('cub=', maps(data, cub))
    print('factorial=', maps(data, factorial))
    print(type(maps))