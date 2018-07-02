# -*- coding: utf-8 -*-
# @Time    : 2018/7/2 22:12
# @Author  : xuanle
# @FileName: qipan2.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine


import turtle

step = 30
length = 4
turtle.hideturtle()
for i in range(-length, length, 1):
    for j in range(-length, length, 1):

        turtle.penup()
        turtle.goto(j * step, i * step)
        turtle.pendown()
        turtle.begin_fill()#开始填充
        for k in range(4):
            if (i + j) % 2 == 0:
                turtle.color("white")
            else:
                turtle.color("black")

            turtle.forward(step)
            turtle.right(90)

        turtle.end_fill()#结束填充

turtle.penup()
turtle.color("black")
turtle.goto(-length * step, -(length+1) * step)
turtle.pendown()
for i in range(4):
    turtle.forward(2 * length * step)
    turtle.right(270)

turtle.done()
