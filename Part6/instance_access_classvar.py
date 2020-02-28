#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 19:22
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : instance_access_classvar.py
# @Software: PyCharm

class test:
    item = 'xxx'
    num = '00000'
    def info(self):
        print('info方法中self.item=', self.item)
        print('info方法中self.num=', self.num)

t = test()
print(t.item)
print(t.num)
t.info()