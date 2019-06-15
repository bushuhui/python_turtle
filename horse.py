import turtle

t = turtle.Turtle()

# Draw a brown house
t.color('brown')

# Draw the base
for i in xrange(4):
    t.forward(50)
    t.left(90)

# Move up
t.penup()
t.left(90)
t.forward(50)
t.pendown()

# Draw the roof
t.right(30)
t.forward(50)
t.right(120)
t.forward(50)
