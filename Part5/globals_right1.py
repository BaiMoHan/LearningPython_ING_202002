#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 15:45
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : globals_right1.py
# @Software:

name = 'Linus'
def test():
    # 通过globals()访问全局变量name
    print(globals()['name'])
    name = 'Jobs'
    print(name)


if __name__ == '__main__':
    test()
    print(name)