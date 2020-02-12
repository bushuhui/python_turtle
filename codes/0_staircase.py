import turtle

def draw():
    turtle.reset()
    turtle.tracer(True)
    turtle.up()
    turtle.backward(100)
    turtle.down()

    # draw 3 squares; the last filled
    turtle.width(3)
    for i in range(3):
        if i == 2:
            turtle.begin_fill()
            #fill(1)
        for _ in range(4):
            turtle.forward(20)
            turtle.left(90)
        if i == 2:
            turtle.color("maroon")
            turtle.end_fill()
            #fill(0)
        turtle.up()
        turtle.forward(30)
        turtle.down()

    turtle.width(1)
    turtle.color("black")

    # move out of the way
    turtle.tracer(False)
    turtle.up()
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(180)
    turtle.down()

    # some text
    turtle.write("startstart", 1)
    turtle.write("start", 1)
    turtle.color("red")

    # staircase
    for i in range(5):
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.right(90)

    # filled staircase
    turtle.tracer(True)
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.right(90)
    turtle.end_fill()


if( __name__ == "__main__" ):
    draw()
    turtle.mainloop()

