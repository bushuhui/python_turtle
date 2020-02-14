
import turtle
from math import cos, sin, gcd
from time import sleep

def draw():
    """
    Spirograph

    ref:
        www.101computing.net/python-turtle-spirograph/
    """
    turtle.tracer(0)

    window = turtle.Screen()
    window.bgcolor("#FFFFFF")

    mySpirograph = turtle.Turtle()
    mySpirograph.hideturtle()
    mySpirograph.speed(0)
    mySpirograph.pensize(2)

    myPen = turtle.Turtle()
    myPen.hideturtle()
    myPen.speed(0)
    myPen.pensize(3)
    myPen.color("#AA00AA")

    (R, r, d) = (125, 75, 125)
    (R, r, d) = (275, 125, 105)
    (R, r, d) = (125, 85, 125)

    angle = 0

    myPen.penup()
    myPen.goto(R - r + d, 0)
    myPen.pendown()

    theta = 0.2
    gcdV = gcd(r, R)
    nRot = min(50, r / gcdV)
    steps = int(nRot * 2 * 3.14 / theta + 1)

    for t in range(0, steps):
        mySpirograph.clear()
        mySpirograph.penup()
        mySpirograph.setheading(0)
        mySpirograph.goto(0, -R)
        mySpirograph.color("#999999")
        mySpirograph.pendown()
        mySpirograph.circle(R)
        angle += theta

        x = (R - r) * cos(angle)
        y = (R - r) * sin(angle)
        mySpirograph.penup()
        mySpirograph.goto(x, y - r)
        mySpirograph.color("#222222")
        mySpirograph.pendown()
        mySpirograph.circle(r)
        mySpirograph.penup()
        mySpirograph.goto(x, y)
        mySpirograph.dot(5)

        x = (R - r) * cos(angle) + d * cos(((R - r) / r) * angle)
        y = (R - r) * sin(angle) - d * sin(((R - r) / r) * angle)
        mySpirograph.pendown()
        mySpirograph.goto(x, y)
        # mySpirograph.setheading((R-r)*degrees(angle)/r)
        # mySpirograph.forward(d)
        mySpirograph.dot(5)
        myPen.goto(mySpirograph.pos())

        mySpirograph.getscreen().update()
        sleep(0.01)

    # Hide Spirograph
    sleep(0.5)
    mySpirograph.clear()
    mySpirograph.getscreen().update()


if __name__ == "__main__":
    draw()
    turtle.mainloop()
