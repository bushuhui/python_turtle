from numpy import *

import numpy as np
from random import random
import turtle


def draw():
    turtle.speed(1)
    turtle.tracer(2, 0)
    turtle.reset()

    x = np.array([[.5], [.5]])
    p = [0.85, 0.92, 0.99, 1.00]
    A1 = np.array([[.85, 0.04],
                [-0.04, .85]])
    b1 = np.array([[0], [1.6]])
    A2 = np.array([[0.20, -0.26],
                [0.23, 0.22]])
    b2 = np.array([[0], [1.6]])
    A3 = np.array([[-0.15, 0.28],
                [0.26, 0.24]])
    b3 = np.array([[0], [0.44]])

    A4 = np.array([[0, 0],
                [0, 0.16]])

    turtle.pensize(1)
    turtle.color("blue")
    cnt = 1
    while True:
        cnt += 1
        if cnt == 4000:
            break

        r = random()
        if r < p [0]:
            x = np.dot(A1, x) + b1
        elif r < p [1]:
            x = np.dot(A2, x) + b2
        elif r < p [2]:
            x = np.dot(A3, x) + b3
        else:
            x = np.dot(A4, x)
        # print x[1]
        turtle.up()
        turtle.goto(x [0] [0] * 50, x [1] [0] * 40 - 200)
        turtle.down()
        turtle.dot(2)


if __name__ == "__main__":
    draw()
    turtle.mainloop()
