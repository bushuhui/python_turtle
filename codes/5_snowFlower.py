# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 14:35:14 2018

@author: Administrator
"""

from turtle import *
from random import *


def ground():
    hideturtle()
    speed(100)
    for i in range(400):
        pensize(randint(35, 50))
        x = randint(-400, 350)
        y = randint(-280, -1)
        r = -y / 280
        g = -y / 280
        b = -y / 280
        pencolor(r, g, b)
        penup()
        goto(x, y)
        pendown()
        forward(randint(40, 100))


def snow():
    hideturtle()
    speed(0)
    pensize(2)
    for i in range(1000):
        r = random()
        g = random()
        b = random()
        pencolor(r, g, b)
        penup()
        setx(randint(-350, 350))
        sety(randint(-270, 270))
        pendown()
        dens = randint(8, 12)
        snowsize = randint(5, 24)
        for j in range(dens):
            forward(snowsize)
            backward(snowsize)
            right(360 / dens)


def draw():
    setup(800, 600, 0, 0)
    tracer(False)
    bgcolor("black")

    snow()
    ground()


if __name__ == "__main__":
    draw()
    mainloop()
