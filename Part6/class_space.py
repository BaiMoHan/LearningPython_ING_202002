#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 17:02
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : class_space.py
# @Software: PyCharm
# 定义全局空间的foo 函数

def foo():
    print("全局空间的foo方法")

# 定义全局空间的bar变量
bar = 20

class Bird:
    # 定义Bird空间的foo 函数
    def foo():
        print("Bird空间的foo方法")
    bar=200


if __name__ == '__main__':
    Bird.foo()
    print(Bird.bar)