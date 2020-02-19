import turtle


def draw():
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    while True:
        turtle.forward(200)
        turtle.left(170)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()


if __name__ == "__main__":
    draw()
    turtle.mainloop()

