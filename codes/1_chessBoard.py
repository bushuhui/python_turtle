import turtle

def drawBlock(p, x, y, l, clBoard, clFill):
    p.penup()
    p.goto(x, y)
    p.color(clBoard, clFill)
    p.seth(0)
    p.pendown()

    p.begin_fill()
    for i in range(4):
        p.forward(l)
        p.left(90)
    p.end_fill()



def draw():
    p = turtle.Pen()
    p.pensize(2)
    p.speed(0)

    begX = -300
    begY = -300
    l = 60
    bi = 0

    # draw outer board
    drawBlock(p, begX, begY, l*10, "black", "white")

    # draw cells
    for iy in range(10):
        for ix in range(10):
            if bi%2 == 0:
                clFill = "black"
            else:
                clFill = "white"

            drawBlock(p,
                      begX+ix*l, begY+iy*l,
                      l,
                      "black", clFill)

            bi = bi + 1

        bi = bi + 1

    p.hideturtle()

if __name__ == "__main__":
    draw()
    turtle.mainloop()
