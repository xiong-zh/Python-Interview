# -*- coding: utf-8 -*- 
# @Time : 2020/1/15 14:57 
# @Author : zhangxiong.net 
# @File : 03.py 
# @Desc :  阅读下面的代码，写出 A0，A1 至 An 的最终值。
#


A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A3 = [A0[s] for s in A0]

A4 = [i for i in A1 if i in A3]
A5 = {i: i * i for i in A1}
A6 = [[i, i * i] for i in A1]

print(A0, A1, A2, A3, A4, A5, A6)

# 结果为
'''
A0 = {'a': 1， 'c': 3， 'b': 2， 'e': 5， 'd': 4}
A1=[0，1，2，3，4，5，6，7，8，9]
A2=[]
A3=[1， 3， 2， 5， 4]
A4=[1， 2， 3， 4， 5]
A5={0:0，1:1，2:4，3:9，4:16，5:25，6:36，7:49，8:64，9:81}
A6 = [[0， 0]， [1， 1]， [2， 4]， [3， 9]， [4， 16]， [5， 25]， [6， 36]，[7， 49]，[8， 64] [9，81]]
'''