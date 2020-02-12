#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 15:13
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : stack_test.py
# @Software: PyCharm
stack = []
# python中有了append函数在尾部追加，因此无为栈另外设置的push函数
stack.append('hello')
stack.append('world')
stack.append('!')
print(stack)
# 第一次出栈
print(stack.pop())
print(stack)
stack.pop()
print(stack)