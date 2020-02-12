# encoding: utf-8

import turtle
import math

def draw():
    # 画出一个圆，填充红色
    r1 = 50

    turtle.setheading(0)

    turtle.up()
    turtle.goto(0, -2*r1)
    turtle.down()

    turtle.begin_fill()
    turtle.color("red")
    turtle.circle(r1*2)
    turtle.end_fill()

    # draw lights
    nl = 12
    r2 = 120
    turtle.width(2)

    for i in range(nl):
        ang = 1.0*i/nl * 2*math.pi
        x1 = r2*math.cos(ang)
        y1 = r2*math.sin(ang)
        x2 = r2*1.5*math.cos(ang)
        y2 = r2*1.5*math.sin(ang)

        turtle.up()
        turtle.goto(x1, y1)
        turtle.down()
        turtle.goto(x2, y2)
        turtle.up()

    # 隐藏光标
    turtle.hideturtle()

if __name__ == "__main__":
    draw()

    # 让程序继续执行
    turtle.mainloop()
