#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 17:13
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : class_static_method.py
# @Software: PyCharm
# 定义 类方法 和 静态方法

class Bird:
    # 使用@classmathod修饰的就是 类方法 ，会自动将第一个参数绑定到类本身
    @classmethod
    def fly(cls):   # 通常类方法的第一个参数名是 cls
        print('类方法fly的cls为:', cls)
    # 使用静态方法，第一个参数不能自动绑定
    @staticmethod
    def info(p):
        print("静态方法info的p为：", p)


if __name__ == '__main__':
    # 调用类方法，第一个参数会自动绑定到类本身
    Bird.fly()
    # 调用静态方法，不会自动绑定，需要手动绑定到第一个参数
    Bird.info('what')
    # 创建对象
    b = Bird()
    # 使用对象调用类方法，第一个参数会自动绑定到类本身
    b.fly()
    # 对象调用静态方法，第一个参数需要手动传入绑定
    b.info('kk')