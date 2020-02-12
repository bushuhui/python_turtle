#!/usr/bin/env python

import turtle

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

def draw():
    t = turtle.Pen()
    t.speed(50)
    t.hideturtle()

    for x in range(360):
        t.pencolor(colors[x % 6])
        t.width(x / 100 + 1)
        t.forward(x)
        t.left(60)


if __name__ == "__main__":
    draw()
    turtle.mainloop()
