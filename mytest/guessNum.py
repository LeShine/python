# -*- coding: utf-8 -*-
# @Time    : 2018/7/1 16:49
# @Author  : xuanle
# @FileName: guessNum.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine


import random

rand = random.randint(1, 1000)
num = eval(input("please input a num:"))

while num != rand:
    if num > rand:
        print("大了")
    else:
        print("小了")
    num = eval(input("please input a num again:"))
else:
    print(rand, "=", num)
