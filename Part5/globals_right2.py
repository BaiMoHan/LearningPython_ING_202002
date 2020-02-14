#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 15:48
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : globals_right2.py
# @Software: PyCharm
name = 'Linus'
def test():
    # 在函数中声明全局变量，后面赋值语句不会定义局部变量，而是改变全局变量
    global name
    print(name)
    name = 'Jobs'


if __name__ == '__main__':
    test()
    print(name)