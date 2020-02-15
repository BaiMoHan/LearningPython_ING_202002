#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/15 11:48
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : Dog.py
# @Software: PyCharm


class Dog:
    def jump(self):
        print('do jump')

    def run(self):
        # 使用self参数引用run()方法的对象
        self.jump()
        print('do run')
        # python对象的一个方法调用另一个方法时，不可以省略self


if __name__ == '__main__':
    dog = Dog()
    dog.jump()
    dog.run()