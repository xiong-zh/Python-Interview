# -*- coding: utf-8 -*- 
# @Time : 2020/1/15 15:11 
# @Author : zhangxiong.net 
# @File : bubbling.py 
# @Desc : 
#

def bubble_sorrt(alist):
    for j in range(len(alist) - 1, 0, -1):
        for i in range(j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1], alist[i]


li = [54, 26, 93, 17, 77, 31, 44, 55, 20]

bubble_sorrt(li)
