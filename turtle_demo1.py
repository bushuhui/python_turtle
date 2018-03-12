from turtle import *

def demo1():
    """Demo of old turtle.py - module"""
    reset()
    tracer(True)
    up()
    backward(100)
    down()
    # draw 3 squares; the last filled
    width(3)
    for i in range(3):
        if i == 2:
            fill(1)
        for _ in range(4):
            forward(20)
            left(90)
        if i == 2:
            color("maroon")
            fill(0)
        up()
        forward(30)
        down()
    width(1)
    color("black")

    # move out of the way
    tracer(False)
    up()
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(180)
    down()

    # some text
    write("startstart", 1)
    write("start", 1)
    color("red")

    # staircase
    for i in range(5):
        forward(20)
        left(90)
        forward(20)
        right(90)

    # filled staircase
    tracer(True)
    fill(1)
    for i in range(5):
        forward(20)
        left(90)
        forward(20)
        right(90)
    fill(0)

    # more text

if( __name__ == "__main__" ):
    demo1()
    done()

