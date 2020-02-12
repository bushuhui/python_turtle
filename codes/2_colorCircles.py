
import turtle
from random import randint

coltab = ["orange", "blue", "green", "purple", "dark blue"]

def draw():
    turtle.speed(0)
    turtle.hideturtle()

    r = 150
    for j in range(1):
        for i in range(18):
            col = coltab[i % 5]
            turtle.pencolor(col)

            turtle.circle(r)
            turtle.left(20)

        r += 50

if __name__ == "__main__":
    draw()
    turtle.mainloop()
