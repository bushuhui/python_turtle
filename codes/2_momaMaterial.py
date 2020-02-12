'''
'''

import turtle
import random
#from FinalDesign import *


# 画任意多边形，其中l为边长，n为边的个数
# 计算机中规定36条边是圆
def polygon(pen, l, n) :
    angle = 360.0 / n
    for i in range(n) :
        pen.forward(l)
        pen.right(angle)

# 画五角星
def star(pen, l, n=5) :
    #turtle.fillcolor('red')
    #turtle.begin_fill()
    for i in range(n) :
        pen.forward(l)
        pen.right(144)
    #turtle.end_fill()

def draw():
    """
    Author:Ariel Margolin
    Date:11/2/15
    Project Title: MOMA Material

    Ref:
        https://sites.google.com/site/ccna1amargolin92/home/sem-1/sem-1-python-video-gaming/python-finale

    FIXME: `polygon`, and `star` functions are not correct

    :return:
    """

    bob=turtle.Turtle()
    turtle.tracer(0)
    turtle.bgcolor("black")

    for y in range(15):
        xpos=random.randint(-100,100)
        ypos=random.randint(-100,100)

        col1=random.random()%256
        col2=random.random()%256
        col3=random.random()%256
        col=(col1,col2,col3)

        bob.penup()
        bob.goto(xpos,ypos)
        bob.pendown()

        #bob.begin_fill()
        for times in range(2000):
            star(bob, 150)
            bob.left(15)
            bob.color(col)
            bob.pensize(0)\
            #bob.end_fill()
            bob.left(15)


        polygon(bob, 20,  6)

if __name__ == "__main__":
    draw()
    turtle.mainloop()
