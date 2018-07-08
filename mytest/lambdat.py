# -*- coding: utf-8 -*-
# @Time    : 2018/7/5 15:49
# @Author  : xuanle
# @FileName: lambdat.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine


# 匿名函数关键字 lambda

nums = lambda a, b: a + 6

print(1, 2)

(lambda mystr: print(mystr))("你好帅！")


# 变长函数

def addmore(*num):
    sum = 0
    for i in num:
        sum += i
    return sum


print(addmore(1, 2), addmore(1, 2, 3, 4, 5))


