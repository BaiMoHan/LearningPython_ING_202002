#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 9:15
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : decorator_test2.py
# @Software: PyCharm

def func(fn):
    def auth_fn(*args):
        print('权限检查')
        fn(*args)
    return auth_fn

@func
def test(a, b):
    print('执行test，a=%s,b=%s' % (a, b))


if __name__ == '__main__':
    test(4, 6)