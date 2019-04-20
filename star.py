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


for i in range(100):
    draw_star(-50+i, 0, 'red')
#draw_star(10, 10, 'green')


turtle.up()
turtle.forward(100)
turtle.goto(-150,-120)
turtle.color("red")
turtle.write("Done")
time.sleep(3)