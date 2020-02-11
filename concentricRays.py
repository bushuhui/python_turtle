# http://www.mrcolson.com/2015/12/09/Python-Art.html

import random
import turtle

# Draws three concentric sets of crooked rays, emerging from darkness

def colorGen(sat = 1, val = 1):
    """Generates random RGB values. sat range 0-1, val range = 0-1"""
    rand1 = round(random.randrange(256)*val)
    rand2 = round(random.randrange(256)*val)
    sat2 = round((1-sat)*255)
    if rand1 >= rand2:
        rand1 = round(255*val)
    else:
        rand2 = round(255*val)
    color = [[sat2, rand1, rand2], [rand1, sat2, rand2], [sat2, rand2, rand1],
             [rand1, rand2, sat2], [rand2, sat2, rand1], [rand2, rand1, sat2]]
    return tuple(color[random.randrange(6)])

def timeTunnel(repeats = 1,zigzag = 10, stepVar = 1):
    for i in range(repeats):
        alex.goto(0,0)
        alex.seth(random.uniform(0,360)) # set heading
        h1 = alex.heading() # get heading
        alex.color(colorGen(val=0))
        for j in range(10):
            alex.down()
            alex.forward(abs(round(random.gauss(10, stepVar),0))) # abs limits motion to forward
            alex.seth(h1 + random.gauss(0,zigzag))
            x = alex.xcor()
            y = alex.ycor()
            alex.color(colorGen(val = j/10))
            h2 = alex.heading()
        for k in range(3):
            alex.down()
            alex.seth(h2 + random.gauss(0, zigzag))
            h3 = alex.heading()
            for k2 in range(10):
                alex.color(colorGen(val = k2/10))
                alex.seth(h3 + random.gauss(0,zigzag))
                alex.forward(abs(round(random.gauss(10, stepVar), 0)))
            alex.up()
            m = alex.xcor()
            n = alex.ycor()
            h4 = alex.heading()
            for l in range(2):
                alex.color(colorGen())
                alex.down()
                alex.seth(abs(h4 + random.gauss(0,zigzag)))
                h5 = alex.heading()
                for l2 in range(10):
                    alex.color(colorGen(val = l2/10))
                    alex.seth(h5 + random.gauss(0,zigzag))
                    alex.forward(abs(round(random.gauss(10,stepVar),0)))
                alex.up()
                alex.goto(m, n)
            alex.goto(x, y)
        alex.up()
        
turtle.tracer(0, 0)
wn = turtle.Screen()
wn.colormode(255)
turtle.bgcolor("black")

alex = turtle.Turtle()
alex.speed(10)
alex.pensize(0)
alex.ht()
timeTunnel(300)
turtle.update()
#wn.exitonclick()
turtle.mainloop()
