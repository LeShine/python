# -*- coding: utf-8 -*-
# @Time    : 2018/7/2 21:35
# @Author  : xuanle
# @FileName: qipan.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine

import turtle

step = 30
length = 4
for i in range(-length, length + 1, 1):
    turtle.penup()
    turtle.goto(-length * step, i * step)
    turtle.pendown()
    turtle.forward(step*2*length)

turtle.right(270)

for i in range(-length, length + 1, 1):
    turtle.penup()
    turtle.goto(i * step, -length * step)
    turtle.pendown()
    turtle.forward(step * 2*length)

turtle.hideturtle()

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.dot(10, "black")
turtle.penup()
turtle.goto(step*4, step*2)
turtle.pendown()
turtle.dot(10, "white")
turtle.done()

