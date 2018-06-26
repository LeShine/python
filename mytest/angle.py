# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 21:44
# @Author  : xuanle
# @FileName: angle.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine


import turtle
import math

x1, y1, x2, y2, x3, y3 = eval(input("请输入三个点坐标"))
a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
b = ((x2 - x3) ** 2 + (y3 - y2) ** 2) ** 0.5
c = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5

A = math.degrees(math.acos((b * b + c * c - a * a) / (2 * b * c)))
B = math.degrees(math.acos((a * a + c * c - b * b) / (2 * a * c)))
C = math.degrees(math.acos((a * a + b * b - c * c) / (2 * a * b)))

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("B " + format(B, ".2f"))

turtle.goto(x2, y2)
turtle.pendown()
turtle.write("C " + format(C, ".2f"))

turtle.goto(x3, y3)
turtle.pendown()
turtle.write("A " + format(A, ".2f"))

turtle.goto(x1, y1)

turtle.hideturtle()
turtle.done()
