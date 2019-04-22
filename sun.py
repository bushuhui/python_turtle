# encoding: utf-8
import turtle

# 移动光标位置
turtle.up()
turtle.goto(0, -90)
turtle.down()

# 画出太阳的光芒，填充黄色
turtle.begin_fill()
turtle.color("yellow")
turtle.circle(200, steps=8)
turtle.end_fill()

# 移动光标位置
turtle.up()
turtle.goto(0, 0)
turtle.down()

# 画出一个圆，填充红色
turtle.begin_fill()
turtle.color("red")
turtle.circle(100)
turtle.end_fill()

# 隐藏光标
turtle.hideturtle()

# 让程序继续执行
turtle.done()
