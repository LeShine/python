# -*- coding: utf-8 -*-
# @Time    : 2018/7/5 9:54
# @Author  : xuanle
# @FileName: global.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine


num = 10  # global 全局变量


def go():
    # global num #引用全局变量
    num = 100  # 局部变量
    print(id(num), num)


go()
print(id(num), num)
print('----------')


def test():
    num = 12

    def testin():
        # nonlocal num  #函数嵌套的外层变量
        num = 120
        print('testin', num, id(num))

    testin()
    print('test', num, id(num))


test()
