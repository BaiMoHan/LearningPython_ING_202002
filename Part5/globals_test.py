#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 15:42
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : globals_test.py
# @Software: PyCharm
name = 'Linus'
def test():
    print(name)
    # name = 'Jobs' 函数体内未定义局部变量name 会报错 函数体内局部变量Hide全局变量
if __name__ == '__main__':
    test()
    print(name)