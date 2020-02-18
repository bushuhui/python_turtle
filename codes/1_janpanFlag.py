import turtle

def draw():
    gordon = turtle.Pen()

    turtle.bgcolor("lightblue")

    # draw cursor to 'turtle'
    gordon.shape("turtle")
    gordon.color("black","white")

    # draw flag
    gordon.begin_fill()
    gordon.forward(150)
    gordon.left(90)

    gordon.forward(100)
    gordon.left(90)

    gordon.forward(150)
    gordon.left(90)

    gordon.forward(400)
    gordon.left(90)
    gordon.end_fill()

    # draw circle
    gordon.color("red","red")
    gordon.penup()
    gordon.goto(75,22)
    gordon.pendown()
    gordon.begin_fill()
    for i in range(180):
        gordon.forward(1)
        gordon.left(2)

    gordon.end_fill()


    gordon.hideturtle()





if __name__ == "__main__":
    draw()

    turtle.mainloop()