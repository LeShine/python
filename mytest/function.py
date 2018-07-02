# -*- coding: utf-8 -*-
# @Time    : 2018/7/2 23:07
# @Author  : xuanle
# @FileName: function.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine

#函数的四种模式


# 无参数，无返回值
def hello():
    print("hello world")


# 有参数，无返回值
def hello_world(name):
    print("hello", name)


# 无参数，有返回值
def pr():
    return "LeShine"


# 有参数，有返回值
def add(num1, num2):
    return num1 + num2


hello()
hello_world("LeShine")
print(pr())
print(add(1, 2))
