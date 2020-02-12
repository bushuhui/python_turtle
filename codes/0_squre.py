import turtle

def draw():
    gordon = turtle.Pen()

    # draw cursor to 'turtle'
    gordon.shape("turtle")

    gordon.forward(100)
    gordon.left(90)

    gordon.forward(100)
    gordon.left(90)

    gordon.forward(100)
    gordon.left(90)

    gordon.forward(100)
    gordon.left(90)


if __name__ == "__main__":
    draw()

    turtle.mainloop()