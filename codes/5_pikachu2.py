#!/usr/bin/env python
# -*- coding:utf-8 -*-
from turtle import *

'''
绘制皮卡丘头部

Ref:
    https://blog.csdn.net/weixin_44517301/article/details/94051615
'''

def face(x, y):
    """画脸"""
    begin_fill()
    penup()
    # 将海龟移动到指定的坐标
    goto(x, y)
    pendown()
    # 设置海龟的方向
    setheading(40)

    circle(-150, 69)
    fillcolor("#FBD624")
    # 将海龟移动到指定的坐标

    penup()
    goto(53.14, 113.29)
    pendown()

    setheading(300)
    circle(-150, 30)
    setheading(295)
    circle(-140, 20)
    print(position())
    forward(5)
    setheading(260)
    circle(-80, 70)
    print(position())
    penup()
    goto(-74.43, -79.09)
    pendown()

    penup()
    # 将海龟移动到指定的坐标
    goto(-144, 103)
    pendown()
    setheading(242)
    circle(110, 35)
    right(10)
    forward(10)
    setheading(250)
    circle(80, 115)
    print(position())

    penup()
    goto(-74.43, -79.09)
    pendown()
    setheading(10)
    penup()
    goto(-144, 103)

    pendown()
    penup()
    goto(x, y)
    pendown()

    end_fill()

    # 下巴
    penup()
    goto(-50, -82.09)
    pendown()
    pencolor("#DDA120")
    fillcolor("#DDA120")
    begin_fill()
    setheading(-12)
    circle(120, 25)
    setheading(-145)
    forward(30)
    setheading(180)
    circle(-20, 20)
    setheading(143)
    forward(30)
    end_fill()
    # penup()
    # # 将海龟移动到指定的坐标
    # goto(0, 0)
    # pendown()


def eye():
    """画眼睛"""
    # 左眼
    color("black", "black")
    penup()
    goto(-110, 27)
    pendown()
    begin_fill()
    setheading(0)
    circle(24)
    end_fill()
    # 左眼仁
    color("white", "white")
    penup()
    goto(-105, 51)
    pendown()
    begin_fill()
    setheading(0)
    circle(10)
    end_fill()
    # 右眼
    color("black", "black")
    penup()
    goto(25, 40)
    pendown()
    begin_fill()
    setheading(0)
    circle(24)
    end_fill()
    # 右眼仁
    color("white", "white")
    penup()
    goto(17, 62)
    pendown()
    begin_fill()
    setheading(0)
    circle(10)
    end_fill()


def cheek():
    """画脸颊"""
    # 右边
    color("#9E4406", "#FE2C21")
    penup()
    goto(-130, -50)
    pendown()
    begin_fill()
    setheading(0)
    circle(27)
    end_fill()

    # 左边
    color("#9E4406", "#FE2C21")
    penup()
    goto(53, -20)
    pendown()
    begin_fill()
    setheading(0)
    circle(27)
    end_fill()


def nose():
    """画鼻子"""
    color("black", "black")
    penup()
    goto(-40, 38)
    pendown()
    begin_fill()
    circle(7, steps=3)
    end_fill()


def mouth():
    """画嘴"""
    color("black", "#F35590")
    # 嘴唇
    penup()
    goto(-10, 22)
    pendown()
    begin_fill()
    setheading(260)
    forward(60)
    circle(-11, 150)
    forward(55)
    print(position())
    penup()
    goto(-38.46, 21.97)
    pendown()
    end_fill()

    # 舌头
    color("#6A070D", "#6A070D")
    begin_fill()
    penup()
    goto(-10.00, 22.00)
    pendown()
    penup()
    goto(-14.29, -1.7)
    pendown()
    penup()
    goto(-52, -5)
    pendown()
    penup()
    goto(-60.40, 12.74)
    pendown()
    penup()
    goto(-38.46, 21.97)
    pendown()
    penup()
    goto(-10.00, 22.00)
    pendown()

    end_fill()

    color("black", "#FFD624")

    penup()
    goto(-78, 15)
    pendown()
    begin_fill()
    setheading(-25)
    for i in range(2):
        setheading(-25)
        circle(35, 70)

    end_fill()
    color("#AB1945", "#AB1945")
    penup()
    goto(-52, -5)
    pendown()
    begin_fill()
    setheading(40)
    circle(-33, 70)
    goto(-16, -1.7)
    penup()
    goto(-18, -17)
    pendown()
    setheading(155)
    circle(25, 70)
    end_fill()


def ear():
    """画耳朵"""
    # 左耳
    color("black", "#FFD624")
    penup()
    goto(-145, 93)
    pendown()
    begin_fill()
    setheading(165)
    circle(-248, 50)
    right(120)
    circle(-248, 50)
    end_fill()
    color("black", "black")
    penup()
    goto(-240, 143)
    pendown()
    begin_fill()
    setheading(107)
    circle(-170, 25)
    left(80)
    circle(229, 15)
    left(120)
    circle(300, 15)
    end_fill()

    # 右耳
    color("black", "#FFD624")
    penup()
    goto(30, 136)
    pendown()
    begin_fill()
    setheading(64)
    circle(-248, 50)

    right(120)
    circle(-248, 50)
    end_fill()
    color("black", "black")
    penup()
    goto(160, 200)
    pendown()
    begin_fill()
    setheading(52)
    circle(170, 25)
    left(116)
    circle(229, 15)
    left(71)
    circle(-300, 15)
    end_fill()

def setting():
    """设置参数"""

    pensize(2)
    # 隐藏海龟
    hideturtle()
    speed(10)


def draw():
    """主函数"""
    setting()
    face(-132, 115)
    eye()
    cheek()
    nose()
    mouth()
    ear()


if __name__ == '__main__':
    draw()
    mainloop()
