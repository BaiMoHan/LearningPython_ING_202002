#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 19:13
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : lambda_in_space.py
# @Software: PyCharm


global_func = lambda x: print('执行lambda表达式,参数x=', x)


class Category:
    func = lambda p : print('执行lambda表达式,参数p=', p)


# 调用全局空间的global_func,传入参数值
global_func('hello')
c = Category()
# 调用类命名空间内的func，python自动绑定第一个参数
c.func()