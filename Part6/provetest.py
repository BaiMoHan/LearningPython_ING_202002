#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 18:42
# @Author  : Baimohan/PH
# @Site    : https://github.com/BaiMoHan
# @File    : provetest.py
# @Software: PyCharm
from time import *
begin_time = time()
l = [2]
m = 2
n = 1000000

for i in range(m, n+1):
    flag = True
    for j in l:
        if i % j == 0:  #如果当前值可整除已筛选出的素数中的任意值，则改变flag，结束循环
            flag = False
            break
    if flag:#添加该数至素数列表
        l.append(i)

txt = open('prove999986.txt', 'w')
mid_time = time()
txt.write(str(mid_time - begin_time))
txt.write('\n\n')
# print(l)
# print(len(l))
# a = []
# f = {}
# n = 1000002
# # 遍历数字
# for i in range(2, n):
#     for x in range(2, n):
#         if i % x == 0:
#             f[i] = f.get(i, 0) + 1
#             print(f[i])

# 取出所有质数
# for i in f:
#     if int(f[i]) == 1:
#         a.append(i)
#     else:
#         pass


def search(l, e):
    left = 0
    right = len(l)
    lenth = right
    while left <= right:
        mid = (left + right) // 2
        if lenth-1 < mid:
            return -2
        elif l[mid] == e:
            return mid
        elif l[mid] > e:
            right = mid - 1
        else:
            left = mid + 1
    return -2


# txt = open('9.txt', 'w')
print('开始')
for a in range(999986, n+1, 2):
    print(a)
    for b in l:
        if b >= a:
            break
        else:
            c = a -b
            if search(l, c) != -2:
                txt.write("%s = %s + %s\n" % (a, b, c))



# # 将所有的质数的算法写入文件
# for i in a:
#     for x in a:
#         l = i + x
#         if l % 2 == 0 and l < n-1 and i >= x:
#             txt.write("%s = %s + %s\n" % (l, i, x))



end_time = time()
run_time = end_time-begin_time
txt.write('\n\n该循环程序运行时间：%s' % run_time)  #该循环程序运行时间：
txt.close()