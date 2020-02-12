import turtle
from math import *


def formulaX(R, r, p, t):
    return (R-r)*cos(t) + p*cos((R-r)/r*t)

def formulaY(R, r, p, t):
    return (R-r)*sin(t) - p*sin((R-r)/r*t)

def t_iterating(R, r, p):
    t = 0

    # move to the first point
    turtle.up()
    turtle.goto(formulaX(R, r, p, t), formulaY(R, r, p, t))
    turtle.down()

    # draw
    while t < 100*pi:
        t = t+0.01
        turtle.goto(formulaX(R, r, p, t), formulaY(R, r, p, t))
    turtle.up()


def draw():
    """

    Ref:
        https://www.geeksforgeeks.org/fractal-using-spirograph-python/
        http://schoolcoders.com/wiki/Spirographs_(Python_implementation)
        https://www.101computing.net/python-turtle-spirograph/

    Parameters:
    R - The radius of the fixed circle
    r = The radius of the moving circle
    p = The offset of the pen point
    """

    turtle.tracer(0, 0)
    turtle.speed(0)

    turtle.color("red")

    #R, r, p = (300, 121, 110)
    R, r, p = (400, 275, 225)
    R, r, p = (400, 270, 125)

    t_iterating(R, r, p)

if __name__ == "__main__":
    draw()
    turtle.mainloop()
