import turtle


def draw():
    turtle.color("red")
    turtle.speed(0)

    # begin draw square loop
    ss = 2
    for i in range(100):
        turtle.forward(ss)
        turtle.right(90)

        ss = ss + 2

    # draw some text
    turtle.up()
    turtle.goto(-20,-120)
    turtle.color("black")
    turtle.write("Squares")

    turtle.hideturtle()


if __name__ == "__main__":
    draw()
    turtle.mainloop()
