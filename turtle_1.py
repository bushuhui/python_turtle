import turtle
import time

wn = turtle.Screen()
wn.colormode(255)

turtle.color("yellow")
#turtle.size(5)
turtle.speed(0)
turtle.goto(0,15)

ss = 1.000001
for i in range(400):
	turtle.forward(ss)
	turtle.right(90)

	ss = ss + 1.5

turtle.up()
turtle.goto(-150,-120)
turtle.color("black")
turtle.write("bushuhui")

turtle.goto(100, 100)
turtle.update()
wn.exitonclick()
