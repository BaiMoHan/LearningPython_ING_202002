#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 16:21
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : function_doc.py
# @Software: PyCharm


def my_max(x, y):   # 把一段字符串放在函数声明后定义前，就是函数的说明文档
    """
    获取两个数值之间较大的函数

    my_max(x,y)
        返回x,y两个参数之间较大的那个数
    :param x:
    :param y:
    :return:
    """
    z = x if x > y else y
    return z


help(my_max)
print(my_max.__doc__)