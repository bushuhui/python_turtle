#!/usr/bin/env python

#
# line & color
#

import turtle




def draw1():
    turtle.bgcolor("lightgreen")
    turtle.speed(4)
    turtle.ht()

    p = turtle.Pen()

    flagHeight = 200

    # color block 1
    p.penup()
    p.goto(50,50)
    p.pendown()

    p.color("black","red")

    p.begin_fill()
    p.forward(100)
    p.left(90)
    p.forward(flagHeight)
    p.left(90)
    p.forward(100)
    p.left(90)
    p.forward(flagHeight)
    p.left(90)
    p.end_fill()

    # color block 2
    p.penup()
    p.goto(-50,50)
    p.pendown()

    p.color("black", "white")

    p.begin_fill()
    p.forward(100)
    p.left(90)
    p.forward(flagHeight)
    p.left(90)
    p.forward(100)
    p.left(90)
    p.forward(flagHeight)
    p.left(90)
    p.end_fill()

    # color block 3
    p.penup()
    p.goto(-150,50)
    p.pendown()

    p.color("black", "blue")

    p.begin_fill()
    p.forward(100)
    p.left(90)
    p.forward(flagHeight)
    p.left(90)
    p.forward(100)
    p.left(90)
    p.pensize(10)
    p.forward(flagHeight)
    p.left(90)
    p.end_fill()

    # draw pole
    p.pensize(10)
    p.right(90)
    p.forward(400)

    p.hideturtle()

def drawBlock(p, w, h):
    p.begin_fill()
    p.forward(w)
    p.left(90)
    p.forward(h)
    p.left(90)
    p.forward(w)
    p.left(90)
    p.forward(h)
    p.left(90)
    p.end_fill()

def draw():
    turtle.bgcolor("lightgreen")
    turtle.speed(4)
    turtle.ht()

    p = turtle.Pen()

    flagWidth  = 100
    flagHeight = 200

    # color block 1
    p.penup()
    p.goto(50,50)
    p.pendown()

    p.color("black","red")
    drawBlock(p, flagWidth, flagHeight)

    # color block 2
    p.penup()
    p.goto(-50,50)
    p.pendown()

    p.color("black", "white")
    drawBlock(p, flagWidth, flagHeight)

    # color block 3
    p.penup()
    p.goto(-150,50)
    p.pendown()

    p.color("black", "blue")
    drawBlock(p, flagWidth, flagHeight)

    # draw pole
    p.pensize(10)
    p.right(90)
    p.backward(flagHeight)
    p.forward(400+flagHeight)

    p.hideturtle()

if __name__ == "__main__":
    draw()
    turtle.mainloop()
