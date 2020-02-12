import turtle
import random

def draw():
    """
    Draws a burst of straight rays, uses a nested loop to make small
        scribbles at the end of each ray

    Ref:
        http://www.mrcolson.com/2015/12/09/Python-Art.html
    """
    turtle.tracer(0, 0)
    wn = turtle.Screen()
    wn.colormode(255)
    turtle.bgcolor("black")

    alex = turtle.Turtle()
    alex.speed(10)
    alex.goto(0,0)
    alex.pensize(0)
    alex.ht()

    for i in range(400):
        alex.color(random.randrange(256),random.randrange(256),random.randrange(256))
        alex.goto(round(random.gauss(0,100),0),round(random.gauss(0,100),0))
        x = alex.xcor()
        y = alex.ycor()
        for j in range(25):
                    s = round(random.gauss(0,5), 0)
                    t = round(random.gauss(0,5), 0)
                    alex.color(random.randrange(256),random.randrange(256),random.randrange(256))
                    alex.pensize(0)
                    alex.goto(x + s, y + t)
        alex.goto(s,t)

    turtle.update()


if __name__ == "__main__":
    draw()
    turtle.mainloop()
