#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 9:30
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : property_test2.py
# @Software: PyCharm


class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def getfullname(self):
        return self.first+','+self.last

    def setfullname(self, fullname):
        fist_last = fullname.rsplit(',')
        self.first = fist_last[0]
        self.last = fist_last[1]

    # 使用property()函数定义fullname属性,只传入两个参数
    # 该属性是读写属性,但不能删除
    fullname = property(getfullname, setfullname)


if __name__ == '__main__':
    u = User('悟空', '孙')
    # 访问fullname属性
    print(u.fullname)
    # 对fullname属性赋值
    u.fullname = '悟饭,孙'
    print(u.first)
    print(u.last)