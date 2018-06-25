import turtle

turtle.pensize(15)  # 笔刷字号

turtle.color('black')
turtle.circle(100)

turtle.penup()  # 笔抬起
turtle.goto(220, 0)  # 笔移动到位置
turtle.pendown()  # 笔放下
turtle.color('red')  # 颜色
turtle.circle(100)  # 画半径为100的圆

turtle.penup()
turtle.goto(-220, 0)
turtle.pendown()
turtle.color('blue')
turtle.circle(100)

turtle.penup()
turtle.goto(-110, -90)
turtle.pendown()
turtle.color('yellow')
turtle.circle(100)

turtle.penup()
turtle.goto(110, -90)
turtle.pendown()
turtle.color('green')
turtle.circle(100)


turtle.done
