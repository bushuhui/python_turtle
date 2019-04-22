import turtle               # allows us to use the turtles library

turtle.speed(1)

wn = turtle.Screen()        # creates a graphics window
alex = turtle.Turtle()      # create a turtle named alex

alex.color('red', 'green')
alex.begin_fill()
alex.shape("turtle")

alex.forward(150)           # tell alex to move forward by 150 units
alex.left(90)               # turn by 90 degrees
alex.forward(75)            # complete the second side of a rectangle
alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(75)            # complete the second side of a rectangle
alex.end_fill()

turtle.done()
