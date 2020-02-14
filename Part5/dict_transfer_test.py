#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 15:18
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : dict_transfer_test.py
# @Software: PyCharm
def swap(dw):
    dw['a'], dw['b'] = dw ['b'], dw['a']
    print('swap:', dw['a'], dw['b'])
    dw = None   # 此行代码可以证明传入列表元组字典的是对这些数据结构的引用，是引用的值传递


if __name__ == '__main__':
    dw = {'a': 6, 'b': 8}
    swap(dw)
    print('main:', dw['a'], dw['b'])
    # 如果需要让函数修改某些主函数数据，可以通过将这些数据包装成列表字典等可变对象，再把可变对象作为参数传入