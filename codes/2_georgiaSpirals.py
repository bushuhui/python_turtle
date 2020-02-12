import turtle
import math
import random


def draw():
    """
    Draw several groups of circles

    :return:
    """

    wn = turtle.Screen()
    wn.bgcolor('black')

    # circle group1
    def drawCircles(t, size):
        for i in range(10):
            t.circle(size)
            size=size-4

    def drawSpecial(t, size, repeat):
      for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)

    Albert = turtle.Turtle()
    Albert.speed(0)
    Albert.color('white')
    drawSpecial(Albert, 100, 10)


    # circle group2
    def drawCircles(t, size):
        for i in range(4):
            t.circle(size)
            size=size-10

    def drawSpecial(t, size, repeat):
        for i in range (repeat):
            drawCircles(t,size)
            t.right(360/repeat)

    Steve = turtle.Turtle()
    Steve.speed(0)
    Steve.color('yellow')
    drawSpecial(Steve,100,10)


    # circle group3
    def drawCircles(t,size):
        for i in range(4):
            t.circle(size)
            size=size-5

    def drawSpecial(t,size,repeat):
        for i in range (repeat):
            drawCircles(t,size)
            t.right(360/repeat)

    Barry = turtle.Turtle()
    Barry.speed(0)
    Barry.color('blue')
    drawSpecial(Barry,100,10)


    # circle group4
    def drawCircles(t,size):
        for i in range(4):
            t.circle(size)
            size=size-19

    def drawSpecial(t,size,repeat):
        for i in range (repeat):
            drawCircles(t,size)
            t.right(360/repeat)

    Terry = turtle.Turtle()
    Terry.speed(0)
    Terry.color('orange')
    drawSpecial(Terry,100,10)


    # circle group5
    def drawCircles(t,size):
        for i in range(4):
            t.circle(size)
            size=size-20

    def drawSpecial(t,size,repeat):
        for i in range (repeat):
            drawCircles(t,size)
            t.right(360/repeat)

    Will = turtle.Turtle()
    Will.speed(0)
    Will.color('pink')
    drawSpecial(Will,100,10)

    turtle.ht()

if __name__ == "__main__":
    draw()
    turtle.mainloop()

