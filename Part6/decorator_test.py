#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 17:24
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : decorator_test.py
# @Software: PyCharm

def deco(fn):
    print('deco')
    fn()  # 执行传入的fn参数 传入的是函数
    return '被修饰函数被替换成返回值'


'''
下面的装饰效果相当于deco(func)
func将会被替换成deco的返回值
'''


@deco
def func():
    print('world')


def foo(fn):
    # 定义一个嵌套函数
    def hunk(*args):  # 参数个数可变
        print('first:', args)
        n = args[0]
        print('second:', n * (n - 1))
        # 查看传给foo函数的fn函数
        print(fn.__name__)
        fn(n * (n - 1))
        print('*' * 15)  # 输出15个*
        return fn(n * (n - 1))

    return hunk


'''
下面的装饰效果相当于foo(test)
test将会被替换成foo的返回值
foo的返回值是hunk函数
所以修饰后test函数就是hunk
'''


@foo
def test(a):
    print('test函数', a)


# 通过函数装饰器为函数提供权限检查的功能
def check(fn):
    def needs(*args):

        # 用一条语句模拟权限检查
        print("---权限检查操作")
        # 回调被修饰的目标函数
        fn(*args)

    return fn


@check
def kid(a, b):
    print("执行kid函数，参数a=%s,b=%s" % (a, b))


if __name__ == '__main__':
    print(func)
    # 被修饰的函数总是被替换成@函数 该函数的返回值
    print(test)
    # 打印test函数，看到的其实是hunk函数
    test(10)
    test(6, 5)
    # 接下来的两次调用test函数本质上还是调用hunk函数
    kid(10, 24)
