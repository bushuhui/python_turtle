# coding: utf-8

import turtle

t = turtle.Turtle()
# speed中参数代表速度快慢，其中0是最快的
# 1-9中，9是最快的
t.speed(0)


# 设置提笔位置
def setpen(x, y):
    # 提笔
    t.penup()
    # 到达指定位置
    t.goto(x, y)
    # 下笔可以画出线条
    t.pendown()
    # 旋转一个角度后恢复到正X轴方向
    t.setheading(0)


# 画三角形
# def draw_triangle(l) :
#     for i in range(3) :
#         t.forward(l)
#         t.right(120)

# 画任意多边形，其中l为边长，n为边的个数
# 计算机中规定36条边是圆
# def polygon(l, n) :
#     angle = 360 / n
#     for i in range(n) :
#         t.forward(l)
#         t.right(angle)

# 画五角星
# def five_star(l) :
#     t.fillcolor('red')
#     t.begin_fill()
#     for i in range(5) :
#         t.forward(l)
#         t.right(144)
#     t.end_fill()

# 画正方形
# def square(x, y, l) :
#     setpen(x, y)
#     for i in range(4) :
#         t.forward(l)
#         t.right(90)

# 画一条正方形
# def square_line(x, y, l, n, d) :
#     for i in range(n) :
#         inner_x = x + (l + d) * i
#         square(inner_x, y, l)

# square_line(-100, 100, 60, 5, 10)

# 画语文作业本
# def square_matrix(x, y, l, n, d, m) :
#     for i in range(m) :
#         inner_y = y - (l + d) * i
#         square_line(x, inner_y, l, n, d)

# square_matrix(-100, 200, 50, 5, 10, 5)
# five_star(100)

# 一个好玩的画
# for i in range(500) :
#     t.forward(i)
#     t.left(91)

def circle(x, y, r, color):
    n = 36
    angle = 360 / n
    pi = 3.1415926535
    c = 2 * pi * r
    l = c / n
    start_x = x - l / 2
    start_y = y + r
    setpen(start_x, start_y)
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(n):
        t.forward(l)
        t.right(angle)
    t.end_fill()


def five_star(l):
    setpen(0, 0)
    t.setheading(162)
    t.forward(150)
    t.setheading(0)
    t.fillcolor('white')
    t.begin_fill()
    t.hideturtle()
    t.penup()
    for i in range(5):
        t.forward(l)
        t.right(144)
    t.end_fill()


def draw():
    circle(0, 0, 300, 'red')
    circle(0, 0, 250, 'white')
    circle(0, 0, 200, 'red')
    circle(0, 0, 150, 'blue')
    five_star(284)


draw()
# 固定弹出框，画完图像后框不直接消失
turtle.done()
