import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")


tess = turtle.Turtle()
tess.color("blue")

size = 20
for i in range(10):
   tess.forward(size)       # Move tess along
   tess.right(10)           #  ...  and turn her

size = 2
for i in range(6):
    tess.forward(size)
    tess.right(28)
    
size = 20
for i in range(10):
   tess.forward(size)       # Move tess along
   tess.left(10)           #  ...  and turn her

size = 2
for i in range(6):
    tess.forward(size)
    tess.right(28)
    

turtle.done()
