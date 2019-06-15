#!/usr/bin/env python

import turtle

t = turtle.Pen()

t.speed(10)
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x / 100 + 1)
    t.forward(x)
    t.left(59)

turtle.mainloop()