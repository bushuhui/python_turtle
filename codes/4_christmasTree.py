from turtle import *
import random
import time


"""
Ref:
    https://blog.csdn.net/weixin_43943977/article/details/102691392
"""


def draw():
    n = 100.0

    speed("fastest")
    screensize(bg='seashell')
    left(90)
    forward(3*n)
    color("orange", "yellow")
    begin_fill()
    left(126)

    for i in range(5):
        forward(n/5)
        right(144)
        forward(n/5)
        left(72)
    end_fill()
    right(126)

    def tree(d, s):
        if d <= 0: return
        forward(s)
        tree(d-1, s*.8)
        right(120)
        tree(d-3, s*.5)
        right(120)
        tree(d-3, s*.5)
        right(120)
        backward(s)


    color("dark green")
    backward(n*4.8)

    tree(15, n)
    backward(n/2)

    for i in range(200):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        up()
        forward(b)
        left(90)
        forward(a)
        down()
        if random.randint(0, 1) == 0:
            color('tomato')
        else:
            color('wheat')
        circle(2)
        up()
        backward(a)
        right(90)
        backward(b)


if __name__ == "__main__":
    draw()
    mainloop()
