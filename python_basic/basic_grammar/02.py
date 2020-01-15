# -*- coding: utf-8 -*- 
# @Time : 2020/1/15 14:51 
# @Author : zhangxiong.net 
# @File : 02.py 
# @Desc : 
#
'''
下面这段代码的输出结果将是什么?请解释?
'''


class Parent(object):
    x = 1


class Child1(Parent):
    pass


class Child2(Parent):
    pass


print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)

'''
结果为:
1 1 1 # 继承自父类的类属性 x，所以都一样，指向同一块内存地址。 
1 2 1 # 更改 Child1，Child1 的 x 指向了新的内存地址。
3 2 3 # 更改 Parent，Parent 的 x 指向了新的内存地址。
'''
