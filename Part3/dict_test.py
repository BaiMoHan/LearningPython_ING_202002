#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 15:48
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : dict_test.py
# @Software: PyCharm
scores = {'chinese': 89}
print(scores['chinese'])
# 对不存在的key赋值就是添加key-value对
scores['math'] = 96
print(scores)
scores[95] = 2
print(scores)
print('math' in scores)
del scores['chinese']
del scores['math']
print(scores)
print('math' not in scores)
print(95 in scores)
