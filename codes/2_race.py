
import turtle

def draw():
    tri = turtle.getturtle()
    tri.resizemode("auto")
    tri.shape("classic")
    tri.up()
    tri.goto(300, -200)
    tri.down()

    rabbit = turtle.Turtle()
    rabbit.resizemode("auto")
    rabbit.shape("turtle")
    rabbit.reset()
    rabbit.left(90)
    rabbit.speed(0)
    rabbit.up()
    rabbit.goto(360, 0)
    rabbit.setheading(90)
    rabbit.down()
    rabbit.speed(6)
    rabbit.color("blue", "orange")
    rabbit.pensize(2)

    tri.speed(6)
    tri.setheading(tri.towards(rabbit))
    count = 1
    while tri.distance(rabbit) > 2:
        rabbit.fd(20.20)
        rabbit.lt(3.2)

        tri.setheading(tri.towards(rabbit))
        tri.fd(20.6)

        if count % 20 == 0:
            pass
            #rabbit.stamp()
            #tri.stamp()
            #switchpen()
        count += 1

    tri.write("CAUGHT! ", font=("Arial", 16, "bold"), align="right")
    tri.pencolor("black")
    tri.pencolor("red")

if __name__ == "__main__":
    draw()
    turtle.mainloop()
