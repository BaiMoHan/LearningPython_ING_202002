#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 12:10
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : for_expr.py
# @Software: PyCharm
a_range = range(10)
# 对a_range执行for表达式
a_list = [x * x for x in a_range]   # for表达式最终返回的是列表,for表达式也叫列表推导式
print(a_list)

# 添加if的for表达式
b_list = [x * x for x in a_range if x % 2 == 0]
print(b_list)
# 将for表达式的方括号改成圆括号，生成一个生成器generator，该生成器也可以用for进行迭代
c_generator = (x * x for x in a_range if x % 2 == 0)
print(c_generator)
for i in  c_generator:
    print('i=', i,end='\t')
print()
# 多个循环的for表达式
d_list = [(x, y) for x in range(5) for y in range(4)]
# d_list列表包含20个列表
print(d_list)
# 三层嵌套的for表达式
e_list = [[x, y, z] for x in range(5) for y in range(3) for z in range(4)]
print(e_list)
src_a = [30, 12, 66, 34, 39, 78, 36, 57, 121]
src_b = [3, 5, 7, 11]
result = [(x, y) for x in src_b for y in src_a if not y % x]
print(result)