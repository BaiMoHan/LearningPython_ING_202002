#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 12:37
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : zip_test.py
# @Software: PyCharm
a = ['a', 'b', 'c']
b = [1, 2, 3]
print([x for x in zip(a,b)])
# zip函数可以将两个列表压缩成一个zip对象且可迭代的,可迭代的对象是一个元组,一一配对
books = ['fluent python', 'python cook book', 'first python']
prices = [140, 100, 99]
for book, price in zip(books, prices):
    print("%s的价格是%s" % (book, price))
# 反向遍历借助reversed()函数
a = range(10)
print([x for x in reversed(a)])
print(a)
b = ['a', 'git', '踩踩', '康康']
print([x for x in reversed(b)])
c = 'hello world'
print([x for x in reversed(c)])
