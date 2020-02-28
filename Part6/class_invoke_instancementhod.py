#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 17:06
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : class_invoke_instancementhod.py
# @Software: PyCharm

class User:
    def walk(self):
        print(self, "正在慢慢行走")


if __name__ == '__main__':
    User.walk('u')  # 未绑定方法，直接调用类方法并传递所需要的参数
    k =User()   # 实例化一个对象，显式地为类方法的一个参数进行绑定
    User.walk(k)