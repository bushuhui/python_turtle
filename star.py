#!/usr/bin/env python

import turtle
import time

turtle.color("purple")
turtle.pensize(5)
turtle.goto(0, 0)
turtle.speed(10)
for i in range(6):
    turtle.forward(100)
    turtle.right(144)

turtle.up()
turtle.forward(100)
turtle.goto(-150,-120)
turtle.color("red")
turtle.write("Done")
time.sleep(3)