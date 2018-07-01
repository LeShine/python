# -*- coding: utf-8 -*-
# @Time    : 2018/7/1 16:38
# @Author  : xuanle
# @FileName: 循环画图.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine

import turtle

times = 0
length = 100

'''
while times < 5:
    turtle.penup()
    turtle.goto(length, length)
    turtle.pendown()
    turtle.goto(length, -length)
    turtle.goto(-length, -length)
    turtle.goto(-length, length)
    turtle.goto(length, length)
    
    times += 1
    length += 50

else:
    print("绘制完成")
    
turtle.done()

'''

for i in range(1, 6): #range(begin,end,step) ==  [1, 6)  begin step 可选 默认为0和1
    turtle.penup()
    turtle.goto(length, length)
    turtle.pendown()
    turtle.goto(length, -length)
    turtle.goto(-length, -length)
    turtle.goto(-length, length)
    turtle.goto(length, length)

    times += 1
    length += 50

turtle.done()


