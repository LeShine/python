# -*- coding: utf-8 -*-
# @Time    : 2018/7/2 10:44
# @Author  : xuanle
# @FileName: lifangti.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine


import turtle
import random

x, y = 100, 100
length = 200

for i in range(3):
    # turtle.color()

    turtle.penup()
    turtle.goto(-x, y)
    turtle.pendown()
    turtle.goto(-x + length, y)
    turtle.goto(-x + length, y - length)
    turtle.goto(-x, y - length)
    turtle.goto(-x, y)

    turtle.goto(-x / 5, y / 5)
    turtle.goto(-x / 5 + length, y / 5)
    turtle.goto(-x / 5 + length, y / 5 - length)
    turtle.goto(-x / 5, y / 5 - length)
    turtle.goto(-x / 5, y / 5)

    turtle.penup()
    turtle.goto(-x / 5 + length, y / 5)
    turtle.pendown()
    turtle.goto(-x + length, y)

    turtle.penup()
    turtle.goto(-x + length, y - length)
    turtle.pendown()
    turtle.goto(-x / 5 + length, y / 5 - length)

    turtle.penup()
    turtle.goto(-x / 5, y / 5 - length)
    turtle.pendown()
    turtle.goto(-x, y - length)

    x += 50
    y += 50
    length += 100

turtle.done()
