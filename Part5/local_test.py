#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 15:26
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : local_test.py
# @Software: PyCharm
def test():
    age = 20
    print(age)
    print(locals())  # 获得函数内的局部变量字典
    # 通过变量字典访问变量
    print(locals()['age'])
    # 通过遍历字典尝试改变变量的值
    locals()['age'] = 99
    # 检查是否修改成功
    print(age)
    # 通过全局字典来修改全局变量
    globals()['x'] = 19



if __name__ == '__main__':
    test()
    x = 5
    y = 88
    print(globals())
    print(locals())
    print('x=', x)
    print(globals()['x'])
    globals()['x'] = 78
    print(x)
    locals()['x'] = 100
    print(x)

# 只要访问的是全局变量，无论什么方式访问，就可以以这种访问方式来修改值