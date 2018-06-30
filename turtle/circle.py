# -*- coding: utf-8 -*-
# @Time    : 2018/6/30 18:21
# @Author  : xuanle
# @FileName: circle.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine

import turtle

x1, y1, r1 = eval(input("input point x1,y1,r1"))
x2, y2, r2 = eval(input("input point x2,y2,r1"))

turtle.penup()
turtle.goto(x1, y1)
turtle.dot(10, "red")
turtle.penup()
turtle.goto(x1, y1 - r1)
turtle.pendown()
turtle.circle(r1)

turtle.penup()
turtle.goto(x2, y2)
turtle.dot(10, "yellow")
turtle.penup()
turtle.goto(x2, y2 - r2)
turtle.pendown()
turtle.circle(r2)

dis = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
if dis == r1 + r2:
    print("外切")
elif dis > r1 + r2:
    print("外离")
elif dis == abs(r2 - r1):
    print("内切")
elif dis < abs(r2 - r1):
    print("内离")
elif abs(r2 - r1) < dis < r2 + r1:
    print("相交")
else:
    print("没有更多关系了")

# turtle.dot(10, "red")  # dot(size,color)
# turtle.penup()
# turtle.goto(0, -100)
# turtle.pendown()
# turtle.circle(100)


turtle.done()
