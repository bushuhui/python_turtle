'''
Author:Ariel Margolin
Date:11/2/15
Project Title:MOMA Material

https://sites.google.com/site/ccna1amargolin92/home/sem-1/sem-1-python-video-gaming/python-finale
'''

import turtle
import random
from FinalDesign import *

bob=turtle.Turtle()
turtle.tracer(0)
turtle.bgcolor("black")
for y in range(15):
    xpos=random.randint(-100,100)
    ypos=random.randint(-100,100)

    col1=random.random()
    col2=random.random()
    col3=random.random()
    col=(col1,col2,col3)

    bob.penup()
    bob.goto(xpos,ypos)
    bob.pendown()
    #bob.begin_fill()
    for times in range(2000):
        star(bob,11,150)
        bob.left(15)
        bob.color(col)
        bob.pensize(0)\
        #bob.end_fill()
        bob.left(15)
        

    polygon(bob,6,20)
