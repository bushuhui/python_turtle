
import turtle

def draw():
    def curvemove():
        for i in range(200):
            turtle.right(1)
            turtle.forward(1)

    turtle.speed(0)
    #turtle.tracer(2, 0)
    turtle.hideturtle()

    turtle.color('red','pink')
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(111.65)
    curvemove()
    turtle.left(120)
    curvemove()
    turtle.forward(111.65)
    turtle.end_fill()


if __name__ == "__main__":
    draw()
    turtle.mainloop()

