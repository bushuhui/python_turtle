
import turtle

# 画三角形
def triangle(l) :
    for i in range(3) :
        turtle.forward(l)
        turtle.right(120)

# 画任意多边形，其中l为边长，n为边的个数
# 计算机中规定36条边是圆
def polygon(l, n) :
    angle = 360.0 / n
    for i in range(n) :
        turtle.forward(l)
        turtle.right(angle)

# 画五角星
def five_star(l) :
    #turtle.fillcolor('red')
    #turtle.begin_fill()
    for i in range(5) :
        turtle.forward(l)
        turtle.right(144)
    #turtle.end_fill()

# 画正方形
def square(x, y, l):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(4) :
        turtle.forward(l)
        turtle.right(90)

# 画一行正方形
def square_line(x, y, l, n, d) :
    for i in range(n) :
        inner_x = x + (l + d) * i
        square(inner_x, y, l)

# 多行正方形
def square_matrix(x, y, l, n, d, m) :
    for i in range(m) :
        inner_y = y - (l + d) * i
        square_line(x, inner_y, l, n, d)


def draw():
    turtle.speed(0)

    # a line of squares
    square_line(-200, 300, 50, 5, 10)

    # a matrix of squares
    square_matrix(-200, 200, 50, 5, 10, 5)

    # a five star
    turtle.penup()
    turtle.goto(-200, -150)
    turtle.pendown()
    five_star(100)

    # a triangle
    turtle.penup()
    turtle.goto(-50, -150)
    turtle.pendown()
    triangle(100)

    # a polygon
    turtle.penup()
    turtle.goto(160, -150)
    turtle.pendown()
    polygon(100, 6)


if __name__ == "__main__":
    draw()

    turtle.mainloop()