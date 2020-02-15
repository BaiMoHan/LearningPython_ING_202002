#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/15 10:48
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : Person.py
# @Software: PyCharm


class Person:
    hair = 'black'

    def __init__(self, name='John', age=16):
        self.name = name
        self.age = age

    def say(self, conten):
        print(conten)


def info(self):     # 实际上self名字也不会自动绑定对象作为调用者
    print('------info函数--------', self)


def intro_func(self, content):
    print('message=', content)


if __name__ == '__main__':
    # Person p; 这是C++的写法
    P = Person()    # 调用Person类构造方法，返回一个Person对象
    print('P:', P)
    # 输出P的name 和 age
    print(P.name, P.age)
    # 访问P的实例变量，并赋值
    P.name = 'Ada'
    P.say('learning python')
    print(P.name, P.age)
    # 为P对象增加一个skills实例变量
    P.skills = ['playing', 'running']   # P对象动态增加方法
    print(P.skills)
    # 删除P对象的name实例变量
    '''
    del P.name
    # 再次访问name
    print(P.name) # 报错
    '''
    # 动态增加的方法不会自动生成self，调用者不会自动绑定对象
    P.foo = info
    # python不会自动将调用者绑定为第一个参数
    # 因此程序需要手动将调用者绑定到第一个参数
    P.foo(P)
    # 使用 lambda 表达式为P对象的bar方法赋值（动态增加方法）
    P.bar = lambda self: print('---------lambda表达式------', self)
    P.bar(P)

    # 借助types模块下的MethodType进行包装，可以使动态增加的方法自动绑定到第一个参数
    # 导入MethodType模块
    from types import MethodType
    # 使用MethodType对intro_func进行包装，将该函数的第一个参数绑定为P
    P.intro = MethodType(intro_func, P)     # 包装时指定了将函数的第一个参数绑定为P
    # 此时第一个参数已经绑定了，无需传入
    P.intro("welcome")