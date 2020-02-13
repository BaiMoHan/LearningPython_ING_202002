#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 16:45
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : default_param_test.py
# @Software: PyCharm


def say_hi(name = 'Linus', message = 'welcome'):
    print(name, '您好！')
    print('消息是：', message)

if __name__ == '__main__':
    say_hi()    # 全部使用默认参数
    say_hi('Knuth','Turing Price')
    say_hi('Turing')
    say_hi(message='666')