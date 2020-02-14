# coding=utf-8
import turtle
import time


def draw():
    # 同时设置pencolor=color1, fillcolor=color2
    turtle.color("red", "yellow")

    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()

    for _ in range(36):
        turtle.forward(200)
        turtle.left(170)

    turtle.ht()

if __name__ == "__main__":
    draw()
    turtle.mainloop()
