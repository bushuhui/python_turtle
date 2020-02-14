import turtle



def draw():
    turtle.colormode(255)
    turtle.pencolor("green")
    turtle.pensize(3)

    laenge = 10

    for i in range(-2, 26):
        for _ in range(3):
            turtle.fd(laenge)
            turtle.lt(120)
        laenge += 10
        turtle.lt(15)

    turtle.ht()

if( __name__ == "__main__" ):
    draw()
    turtle.mainloop()
