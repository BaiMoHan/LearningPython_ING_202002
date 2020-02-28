#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 19:17
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : class_var.py
# @Software: PyCharm

class Address:
    detail = 'China'
    post_code = 'xxxx'
    def info(self):
        # 尝试访问类变量
        # print(detail) 报错
        print(Address.detail)
        print(Address.post_code)


# 通过类来访问Address的类变量
print(Address.detail)
addr = Address() # 实例化对象
addr.info()
# 修改Address的类变量
Address.detail = 'Russian'
Address.post_code = 'yyy'
addr.info()