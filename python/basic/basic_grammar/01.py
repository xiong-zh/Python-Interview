# -*- coding: utf-8 -*- 
# @Time : 2020/1/15 14:47 
# @Author : zhangxiong.net 
# @File : 01.py 
# @Desc : 
#
'''
a=1,b=2,不用中间变量交换 a 和 b 的值?
'''

a = 1
b = 2

a = a + b
b = a - b
a = a - b

a = a ^ b
b = b ^ a
a = a ^ b

a, b = b, a
