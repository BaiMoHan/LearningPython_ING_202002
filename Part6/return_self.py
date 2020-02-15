#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/15 12:18
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : return_self.py
# @Software: PyCharm


class ReturnSelf:
    def grow(self):
        if hasattr(self,'age'):
            self.age += 1
        else:
            self.age = 1
        return self
    # 把self作为返回指可以让代码更简洁，但可能造成实际意义的模糊


if __name__ == '__main__':
    rs = ReturnSelf()
    # 可以连续调用同一个方法
    rs.grow().grow().grow()
    print('rs:age=', rs.age)
    help(hasattr)