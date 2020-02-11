# http://www.mrcolson.com/2015/12/09/Python-Art.html

import random
import turtle

# Draws three sets of concentric rays with a sort of spiral galaxy effect.
# Small step size and multiple nested loops runs quite slowly. Probably not the most efficient code.

def hueGen2(hue = 0, val = 1, sat=1):
    """Generates a 360 degree range of hues
    sat of 1 is full saturation, 0 is B & W.
    val of 1 is full color, 0 is black"""
    hue = float(hue)
    val = float(val)
    sat = float(sat)

    if 0 <= hue < 60:
        r = 1.0
        g = (hue/59.0) + (1.0-sat)*(59.0-hue)/59.0
        b = 1.0 - sat
        hueOut = (r*val, g*val, b*val)
    elif 60 <= hue < 120:
        r = ((1.0 - 1.0*(hue-60.0)/59.0) + 1.0*(1.0-sat)*(1.0-(119.0-hue)/59.0))
        g = 1.0
        b = 1.0 - sat
        hueOut = (r*val, g*val, b*val)
    elif 120 <= hue < 180:
        r = 1.0 - sat
        g = 1.0
        b = (1.0*(hue-120.0)/59.0) + (1.0-sat)*(179.0-hue)/59.0
        hueOut = (r*val, g*val, b*val)
    elif 180 <= hue < 240:
        r = 1.0 - sat
        g = (1.0-1.0*(hue-180)/59.0) + 1.0*(1-sat)*(1.0 - 1.0*(239-hue)/59.0)
        b = 1.0
        hueOut = (r*val, g*val, b*val)
    elif 240 <= hue < 300:
        r = (1.0*(hue-240.0)/59.0) + 1.0*(1-sat)*(299.0-hue)/59.0
        g = 1.0 - sat
        b = 1.0
        hueOut = (r*val, g*val, b*val)
    elif 300 <= hue < 360:
        r = 1.0
        g = 1.0 - sat
        b = (1.0-1.0*(hue-300)/59.0) + 1.0*(1-sat)*(1-1.0*(359-hue)/59.0)
        hueOut = (r*val, g*val, b*val)
    elif hue >= 360:
        hueOut = hueGen(hue % 360, val, sat)

    hueOut_ = [min(255, int(255*hueOut[i])) for i in range(3)]
    return hueOut_

def hueGen(hue = 0,val = 1, sat=1):
    """Generates a 360 degree range of hues
    sat of 1 is full saturation, 0 is B & W.
    val of 1 is full color, 0 is black"""
    if 0 <= hue < 60:
        r = 1
        g = (hue/59) + (1-sat)*(59-hue)/59
        b = 1 - sat
        hueOut = (r*val,g*val,b*val)
    elif 60 <= hue < 120:
        r = ((1-(hue-60)/59) + (1-sat)*(1-(119-hue)/59))
        g = 1
        b = 1 - sat
        hueOut = (r*val,g*val,b*val)
    elif 120 <= hue < 180:
        r = 1 - sat
        g = 1
        b = ((hue-120)/59) + (1-sat)*(179-hue)/59
        hueOut = (r*val,g*val,b*val)
    elif 180 <= hue < 240:
        r = 1 - sat
        g = (1-(hue-180)/59) + (1-sat)*(1-(239-hue)/59)
        b = 1
        hueOut = (r*val,g*val,b*val)
    elif 240 <= hue < 300:
        r = ((hue-240)/59) + (1-sat)*(299-hue)/59
        g = 1 - sat
        b = 1
        hueOut = (r*val,g*val,b*val)
    elif 300 <= hue < 360:
        r = 1
        g = 1 - sat
        b = (1-(hue-300)/59) + (1-sat)*(1-(359-hue)/59)
        hueOut = (r*val,g*val,b*val)
    elif hue >= 360:
        hueOut = hueGen(hue % 360, val, sat)
    return hueOut

def timeTunnel(repeats = 1, zigzag = 10,  stepVar = 1,  curve = 0):
    """
    Draws fuzzy concentric circles.
        zigzag is sd of randomgauss,
        stepVar is sd of length,
        curve is a multiplier that gives a spiral effect
    """
    foo = 0
    for i in range(repeats):
        print("loop [%6d / %6d]" % (i, repeats))

        alex.goto(0,0)
        alex.seth(random.uniform(0,360)) # set heading
        h1 = alex.heading() # get heading
        alex.color(hueGen(hue = i))
        for j in range(50):
            alex.down()
            alex.forward(abs(round(random.gauss(2, stepVar),0))) # abs limits motion to forward
            alex.seth(h1 + curve*j + random.gauss(0,4*zigzag))
            x = alex.xcor()
            y = alex.ycor()
            alex.color(hueGen(hue = i*j, val = 1.0*j/50)) # 1 - 51
            h2 = alex.heading()
        for k in range(2):
            alex.down()
            alex.seth(h2)
            for k2 in range(50):
                alex.color(hueGen(hue = i+j+k*k2, val = 1.0*k2/50))
                alex.seth(h2 + curve*k2 + random.gauss(0,2*zigzag))
                alex.forward(abs(round(random.gauss(2, stepVar), 0)))
            alex.up()
            m = alex.xcor()
            n = alex.ycor()
            h3 = alex.heading()
            # h4 = alex.heading()
            for l in range(4):
                alex.color(hueGen(hue = 9*l))
                alex.down()
                alex.seth(h3)
                # h5 = alex.heading()
                for l2 in range(50):
                    alex.color(hueGen(hue = l*l2*2.449, val = 1.0*l2/50))
                    alex.seth(h3 + curve*l2 + random.gauss(0,zigzag))
                    alex.forward(abs(round(random.gauss(2,stepVar),0)))
                alex.up()
                alex.goto(m, n)
            alex.goto(x, y)
        alex.up()

turtle.tracer(0, 0)
wn = turtle.Screen()

# default color mode is (0, 1), therefore, use hueGen
# if set color mode to 255, then use hueGen2
#wn.colormode(255)

turtle.bgcolor("black")
alex = turtle.Turtle()
alex.speed(10)
alex.pensize(0)
alex.ht()
timeTunnel(100,1, 1, .5)
print("Finished draw")

turtle.update()

saveImage = False
if saveImage:
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="concentricRay2.eps")

#wn.exitonclick()
turtle.mainloop()
