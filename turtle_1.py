import turtle
import time

turtle.color("purple")
#turtle.size(5)
turtle.speed(1)
turtle.goto(0,0)
for i in range(4):
	turtle.forward(100)
	turtle.right(90)
turtle.up()
turtle.goto(-150,-120)
turtle.color("red")
turtle.write("Done")
time.sleep(999)

turtle.goto(100, 100)
