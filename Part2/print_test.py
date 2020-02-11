#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 14:44
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : print_test.py
# @Software: PyCharm
user_name = "bai mo han"
use_age = 20
print("开发者：", user_name, "年龄：", use_age)
# 同时输出多个变量和字符串，指定分隔符
print("开发者：", user_name, "年龄：", use_age, sep='|')
# 设置end参数,输出后不在换行
print("开发者：", user_name, "年龄：", use_age, end='')
print("没有换行")
# file参数的默认值未sys.stdout，可以改成文件
f = open("poem.txt","w") # 打开文件写入
print("床前明月光", file=f)
print("疑是地上霜", file=f)