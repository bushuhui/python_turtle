import turtle
from math import *


def formulaX(R, r, p, t):
    return (R-r)*cos(t) - (r+p)*cos((R-r)/r*t)

def formulaY(R, r, p, t):
    return (R-r)*sin(t) - (r+p)*sin((R-r)/r*t)

def t_iterating(R, r, p):
    t = 0
    turtle.down()

    while t < 20*pi:
        t = t+0.01
        turtle.goto(formulaX(R, r, p, t), formulaY(R, r, p, t))
    turtle.up()


def main():
    """
    R = int(input("The radius of the fixed circle: "))
    r = int(input("The radius of the moving circle: "))
    p = int(input("The offset of the pen point, between <10 - 100>: "))
    """
    R = 300
    r = 100
    p = 20

    if p < 10 or p > 100:
        input("Incorrect value for p!")

    t_iterating(R, r, p)
    turtle.done()


main()