#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 13:53
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : num_to_rmb.py
# @Software: PyCharm
"""
    把一个浮点数分解成整数部分和小数部分
    num是需要分解的浮点数
    第一个数组元素是整数部分，第二个数组元素是小数部分
"""


def divide(num):
    # 将一个浮点数强制转换为int类型从而得到整数部分
    integer = int(num)
    # 浮点数减去整数部分即得到小数部分,乘以100取整可以得到两位小数
    fraction = round((num - integer) * 100)
    # 把整数转为字符串
    return str(integer), str(fraction)


han_list = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖', '拾']
unit_list = ['十', '百', '千']
'''
把一个四位的数字字符串变成汉字字符串
num_str是需要转换的4位数字字符串
返回四位数字字符串被转换为汉字字符串
'''


def four_to_hanster(num_str):
    result = ''
    num_len = len(num_str)
    # 依次遍历数字字符串的每一位数字
    for i in range(num_len):
        # 把字符串转换成是数值
        num = int(num_str[i])
        # 如果不是最后一位数字，而且数字不是零则需要添加单位
        if i != num_len - 1 and num != 0:
            result += han_list[num] + unit_list[num_len - 2 - i]
        # 否则不要添加单位
        else:
            result += han_list[num]
    return result


'''
把数字字符串变成汉字字符串
num_str是需要被转换的数字字符串
返回数字字符串被转换成汉字字符串
'''

def integer_to_str(num_str):
    str_len = len(num_str)
    if str_len > 12:
        print('数字太大,翻译不了')
        return
    # 如果大于8位，包含单位‘亿’
    elif str_len >8:
        return four_to_hanster(num_str[:-8]) + '亿' +\
            four_to_hanster(num_str[-8:-4]) + '万' +\
            four_to_hanster(num_str[-4:])
    # 如果大于4位,包含单位'万'
    elif str_len > 4:
        return four_to_hanster(num_str[:-4]) + '万'+\
            four_to_hanster(num_str[-4:])
    else:
        return four_to_hanster(num_str)


if __name__ == '__main__':
    num = float(input("请输入一个浮点数："))
    integer, fraction = divide(num)
    print(integer_to_str(integer))
    print(fraction)

