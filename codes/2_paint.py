#!/usr/bin/python

"""       
turtle-example-suite:

            tdemo_paint.py

A simple  eventdriven paint program

- use left mouse button to move turtle
- middle mouse button to change color
- right mouse button do turn filling on/off
 -------------------------------------------
 Play around by clicking into the canvas
 using all three mouse buttons.
 -------------------------------------------
          To exit press STOP button
 -------------------------------------------
"""

from turtle import *

def switchupdown(x=0, y=0):
    if pen()["pendown"]:
        end_fill()
        up()
    else:
        down()
        begin_fill()

def changecolor(x=0, y=0):
    global colors
    colors = colors[1:]+colors[:1]
    color(colors[0])

def draw():
    global colors
    shape("circle")
    resizemode("user")
    shapesize(.5)
    width(3)
    colors=["red", "green", "blue", "yellow"]
    color(colors[0])
    switchupdown()
    onscreenclick(goto,1)
    onscreenclick(changecolor,2)
    onscreenclick(switchupdown,3)
    print("EVENTLOOP")

if __name__ == "__main__":
    draw()
    mainloop()
