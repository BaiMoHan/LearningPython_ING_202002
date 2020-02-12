#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 11:33
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : search_test.py
# @Software: PyCharm

s = 'www.github.com is a good site'
# 判断s是否以www开头
print(s.startswith('www'))
# 判断s是否以site结尾
print(s.endswith('site'))
# 查找s中hub出现的位置
print(s.find('hub'))
# 查找s中hub出现的位置
print(s.index('hub'))
# 从索引8处开始查找hub出现的位置
print(s.find('hub', 8))
# 将字符串中的g换成XXX
print(s.replace('g', 'xxx'))
# 将字符串中的一个g换成xxx
print(s.replace('g', 'xxx', 1))
# 定义翻译表 a->α b->β t->964
table = {97: 945, 98: 946, 116: 964}
print(s.translate(table))
table = str.maketrans('abc', '123')
print(table)
