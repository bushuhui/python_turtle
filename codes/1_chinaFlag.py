import turtle

def draw_n_angle(aTurtle, size=50, num=5, color=None):
    ''' 绘制正n角形，默认为黄色
    args:
      aTurtle: turtle对象实例
      size: int类型，正多角形的边长
      n: int类型，是几角形
      color: str， 图形颜色，默认不填色
    '''
    if color:
        aTurtle.begin_fill()
        aTurtle.fillcolor(color)
    for i in range(num):
        aTurtle.forward(size)
        aTurtle.left(360.0 / num)
        aTurtle.forward(size)
        aTurtle.right(2 * 360.0 / num)
    if color:
        aTurtle.end_fill()

def draw():
    jf = turtle.Pen()
    jf.shape("turtle")
    jf.color("black", "red")

    # draw flag
    jf.begin_fill()

    jf.forward(150)
    jf.left(90)

    jf.forward(100)
    jf.left(90)

    jf.forward(150)
    jf.left(90)

    jf.forward(400)

    jf.end_fill()

    # draw star
    jf.penup()
    jf.goto(10, 70)
    jf.pendown()

    #draw_n_angle(jf, 50, 5, "yellow")

    jf.color("black", "yellow")
    jf.setheading(0)
    jf.begin_fill()

    for i in range(5):
        jf.forward(15)
        jf.left(72)
        jf.forward(15)
        jf.right(144)

    jf.end_fill()


    # small star 1
    jf.penup()
    jf.goto(51, 88)
    jf.pendown()

    jf.color("black", "yellow")
    jf.setheading(0)
    jf.begin_fill()

    for i in range(5):
        jf.forward(8)
        jf.left(72)
        jf.forward(8)
        jf.right(144)

    jf.end_fill()



    # small star 2
    jf.penup()
    jf.goto(57, 65)
    jf.pendown()

    jf.color("black", "yellow")
    jf.setheading(0)
    jf.begin_fill()

    for i in range(5):
        jf.forward(8)
        jf.left(72)
        jf.forward(8)
        jf.right(144)

    jf.end_fill()




    # small star 3
    jf.penup()
    jf.goto(51, 42)
    jf.pendown()

    jf.color("black", "yellow")
    jf.setheading(0)
    jf.begin_fill()

    for i in range(5):
        jf.forward(8)
        jf.left(72)
        jf.forward(8)
        jf.right(144)

    jf.end_fill()





    # small star 4
    jf.penup()
    jf.goto(30, 30)
    jf.pendown()

    jf.color("black", "yellow")
    jf.setheading(0)
    jf.begin_fill()

    for i in range(5):
        jf.forward(8)
        jf.left(72)
        jf.forward(8)
        jf.right(144)

    jf.end_fill()




    jf.hideturtle()


if __name__ == "__main__":
    draw()

    turtle.mainloop()