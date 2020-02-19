from turtle import*

def draw():
    pensize(2)
    color('black','black')

    penup()
    goto(0, -300)
    pendown()

    # outer circle
    begin_fill()
    circle(300)
    end_fill()

    # white-black curve
    begin_fill()
    color('black','white')
    seth(180)
    circle(-300,180)
    circle(-150,180)
    end_fill()

    begin_fill()
    color('black','black')
    circle(150,180)
    end_fill()

    # small circles
    penup()
    goto(0, -200)
    pendown()
    begin_fill()
    color('black','white')
    circle(50)
    end_fill()

    penup()
    goto(0, 100)
    pendown()
    begin_fill()
    color('black', 'black')
    circle(50)
    end_fill()

    hideturtle()


if __name__ == "__main__":
    draw()
    mainloop()
