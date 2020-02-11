#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 15:59
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : bytes_test.py
# @Software: PyCharm
# 创建一个空byte
b1 = bytes()
# 创建一个空byte
b2 = b''
# 通过b前缀指点字符串为byte型的值
b3 = b'hello'
print(b3)
print(b3[0])
print(b3[2:4])
# 调用bytes方法将字符串转为bytes
b4 = bytes("学习python", encoding='utf-8')
print(b4)
# 利用字符串encode方法变成bytes
b5 = "学习python".encode('utf-8')
print(b5)
# 调用bytes对象的decode方法将bytes转为string
st = b5.decode('utf-8')
print(st)