
"""
import turtle


def draw_triangle(some_turtle):
    # This for loop will create - Outer Triangle
    some_turtle.color("green")
    some_turtle.begin_fill()
    for i in range(1, 4):
        some_turtle.forward(50)
        some_turtle.left(120)
        # This for loop will create - Inner Triangle
        for j in range(1, 4):
            some_turtle.forward(25)
            some_turtle.left(120)
            some_turtle.end_fill()


def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")
    # Create the turtle Brad - Draws a Triangle
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("green")
    brad.speed(50)

    # This for loop will create - Inner & Outer Triangle At 120 deg
    for d in range(1, 4):
        brad.left(120)
        # This for loop will create - Inner & Outer Triangle At distance 50
        for c in range(1, 5):
            draw_triangle(brad)
            brad.forward(50)


    window.exitonclick()

draw_art()
"""


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

    # This for loop will create - Inner & Outer Triangle At 120 deg
    for d in range(3):
        brad.left(120)
        # This for loop will create - Inner & Outer Triangle At distance 50
        for c in range(4):
            draw_triangle(brad)
            brad.forward(50)

    brad.hideturtle()

window = turtle.Screen()
window.bgcolor("white")

draw_art()

turtle.mainloop()