#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 15:02
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : varargs4.py
# @Software: PyCharm


def test(name, message):
    print('user:', name)
    print('message:', message)

def foo(name, *nums):
    print('name=', name)
    print("*nums=", nums)

def bar(book, price, desc):
    print(book, '的价格是', price)
    print('message=', desc)


if __name__ == '__main__':  #参数逆向收集
    my_list = ['Linus', 'Great']
    test(*my_list)          # 列表与元组元素拆开传递给函数参数需要在前面加入*，字典需要加入**
    my_tuple = (1, 2, 3)
    foo('Jobs', *my_tuple)
    foo(*my_tuple)      # 参数逆向收集，将元组第一个元素传给第一个参数
    foo(my_tuple)       # 不使用逆向收集，则元素整体传给第一个参数
    my_dic = {'price': 89, 'book': 'fluent python', 'desc': 'great book'}
    # 按照逆向收集的方式传递函数参数，字典需要两个**在前
    bar(**my_dic)