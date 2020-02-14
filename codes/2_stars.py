#!/usr/bin/env python

import turtle
import time
import random


def draw_star(x, y, color):
    turtle.color(color)
    turtle.pensize(1)
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.speed(10)

    for i in range(6):
        turtle.forward(100)
        turtle.right(144)


def draw():
    turtle.speed(0)

    for i in range(5):
        draw_star(0, 0, 'red')

    for i in range(5):
        draw_star(-200, 0, 'green')

    for i in range(5):
        draw_star(200, 0, 'blue')


    turtle.up()
    turtle.forward(100)
    turtle.goto(-150,-120)
    turtle.color("red")
    turtle.write("Done")


if __name__ == "__main__":
    draw()
    turtle.mainloop()
