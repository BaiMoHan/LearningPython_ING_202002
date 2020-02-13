#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 15:09
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : supermarket.py
# @Software: PyCharm

# 定义仓库
repository = dict()
# 定义购物清单对象
shop_list = []

# 定义一个函数来初始化商品
def init_repository():
    # 初始化很多商品,每个元组代表一个商品
    goods1 = ('100001', 'fluent python', 118)
    goods2 = ('100002', 'first python', 48)
    goods3 = ('100003', 'master python', 55)
    goods4 = ('100004', 'python program', 66)
    goods5 = ('100005', 'learning python simply',88)
    goods6 = ('100006', 'classic python', 109)
    # 把商品入库，条码作为key
    repository[goods1[0]] = goods1
    repository[goods2[0]] = goods2
    repository[goods3[0]] = goods3
    repository[goods4[0]] = goods4
    repository[goods5[0]] = goods5
    repository[goods6[0]] = goods6

# 显示超市的商品清单，即遍历仓库的字典
def show_goods():
    print('welcome to book shop')
    print('manu:')
    print("%13s%40s%10s" % ('条码', '商品名称', '单价'))
    # 遍历repository中的value
    for goods in repository.values():
        print('%15s%40s%12s' % goods)

# 显示购物清单，即遍历购物清单的list列表
def show_list():
    print('='*100)
    # 如果购物清单不为空，则输出清单的内容
    if not shop_list:
        print('还未购买商品')
    else:
        title = '%-5s|%15s%40s%10s%4s%10s'%\
                ('ID', '条码', '商品名称', '单价', '数量', '小计')
        print(title)
        print('-'* 100)
        # 记录总计的价钱
        sum = 0
        # 遍历代表购物清单的list列表
        for 