#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/15 12:03
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : self_test.py
# @Software: PyCharm


class User:
    def test(self):
        print('self=', self)


if __name__ == '__main__':
    u = User()
    print(u)
    u.test()
    foo = u.test
    foo()