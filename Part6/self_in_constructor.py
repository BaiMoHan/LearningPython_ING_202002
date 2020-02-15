#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/15 12:00
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : self_in_constructor.py
# @Software: PyCharm


class InConstructor:
    def __init__(self):
        # 在构造方法中定义一个foo变量，局部变量
        foo = 0
        # 使用self代表该构造方法正在初始化的对象
        self.foo = 6
        # 所有使用InConstrutor创建的对象的foo实例变量将被设为6


if __name__ == '__main__':
    print(InConstructor().foo)