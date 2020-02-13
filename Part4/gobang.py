#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 14:45
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : gobang.py
# @Software: PyCharm
# def Count(radium):
#     from math import pi as p
#     C =  2 * p * radium
#     A = p * radium ** 2
#     return C, A
#
#
# if __name__ == '__main__':
#     radium = int(input('Please enter radium:'))
#     Circumference, area = Count(radium)
#     print('Circumference is %.2f' % (Circumference))
#     print('Round area is %.2f' % (area))

# 定义棋盘的大小
BOARD_SIZE = 15
# 定义一个二维列表来充当棋盘
board = []
def initboard():
    # 为每个元素赋值'✛'，用于控制台画出棋盘
    for i in range(BOARD_SIZE):
        row = ['✛'] * BOARD_SIZE
        board.append(row)

# 在控制台输出棋盘
def printBoard():
    # 打印每个列表元素
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            # 打印列表元素后不换行
            print(board[i][j],end='')
        # 每打印完一行输出一个换行
        print()


if __name__ == '__main__':
    initboard()
    printBoard()
    inputStr = input("请输入您下棋的坐标，应以x,y的形式:\n")
    while inputStr != None:
        x_str, y_str = inputStr.split(sep=',')
        # 为对应的列表元素赋值⚪
        board[int(x_str)-1][int(y_str)-1] = '⚪'
        printBoard()
        inputStr = input("请输入您下棋的坐标，应以x,y的形式:\n")