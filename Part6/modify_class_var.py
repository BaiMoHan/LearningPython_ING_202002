#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 20:11
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : modify_class_var.py
# @Software: PyCharm

class test:
    # 类变量
    item = 'xxx'
    num = '296659'
    def func(self, item, num):
        # 下面赋值语句不是对类变量赋值，而是定义新的实例变量
        # 实例变量改变不会影响类变量
        self.item = item
        self.num = num


if __name__ == '__main__':
    t = test()
    t.func('oaiw', '55662')
    print(t.item)
    print(t.num)
    print(test.item)
    print(test.num)
    test.num = '类变量num'
    test.item = '类变量item'
    print(test.num)
    print(test.item)
    print(t.num)
    print(t.item)
    t.item = '实例变量item'
    t.num = '实例变量num'
    print(test.item)
    print(test.num)
    # 类变量与实例变量是两个东西