
import turtle

def draw_triangle(some_turtle):
    # This for loop will create - Outer Triangle
    for i in range(3):
        some_turtle.forward(50)
        some_turtle.left(120)
        # This for loop will create - Inner Triangle
        some_turtle.begin_fill()
        for j in range(3):
            some_turtle.forward(25)
            some_turtle.left(120)
        some_turtle.end_fill()

def draw_art():
    # Create the turtle Brad - Draws a Triangle
    brad = turtle.Turtle(shape="arrow")
    brad.color("green")
    brad.speed("fastest")

    brad.pu()
    brad.goto(100, 0)
    brad.pd()

    # This for loop will create - Inner & Outer Triangle At 120 deg
    for d in range(3):
        brad.left(120)
        # This for loop will create - Inner & Outer Triangle At distance 50
        for c in range(4):
            draw_triangle(brad)
            brad.forward(50)

    brad.hideturtle()


def draw():
    window = turtle.Screen()
    window.bgcolor("white")

    draw_art()


if __name__ == "__main__":
    draw()
    turtle.mainloop()
