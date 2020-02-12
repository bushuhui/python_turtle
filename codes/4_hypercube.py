# draw hypercube https://www.jb51.net/article/142228.htm
# encoding: utf-8

import turtle


# 创建绘制直线函数
def drawLine(p1, p2, size=3, color="black"):
    turtle.penup()
    turtle.goto(p1)
    turtle.pensize(size)
    turtle.pencolor(color)
    turtle.pendown()
    turtle.goto(p2)


def main():
    # 求取点后，将超立方体点分为上下两个部分，两个列表
    a = [[120.71, 50], [50, 120.71], [-50, 120.71], [-120.71, 50], [-50, -20.71], [50, -20.71], [20.71, 50],
         [-20.71, 50]]
    b = [[120.71, -50], [50, 20.71], [-50, 20.71], [-120.71, -50], [-50, -120.71], [50, -120.71], [20.71, -50],
         [-20.71, -50]]

    # 绘制点
    turtle.pencolor("red")
    turtle.penup()
    for i in range(len(a)):
        turtle.goto(a [i])
        turtle.down()
        turtle.dot(10, "red")
        turtle.penup()
    for i in range(len(b)):
        turtle.goto(b [i])
        turtle.down()
        turtle.dot(10, "red")
        turtle.penup()

    # 绘制六边形直线
    for i in range(6):
        if i <= 4:
            drawLine(a [i], a [i + 1])
            drawLine(b [i], b [i + 1])
        else:
            drawLine(a [i], a [0])
            drawLine(b [i], b [0])

    # 绘制竖直线
    for i in range(len(a)):
        drawLine(a [i], b [i])

    # 绘制斜线
    drawLine(a [6], a [0])
    drawLine(a [6], a [2])
    drawLine(a [6], a [4])
    drawLine(a [7], a [1])
    drawLine(a [7], a [3])
    drawLine(a [7], a [5])
    drawLine(b [6], b [0])
    drawLine(b [6], b [2])
    drawLine(b [6], b [4])
    drawLine(b [7], b [1])
    drawLine(b [7], b [3])
    drawLine(b [7], b [5])


if __name__ == '__main__':
    main()
    turtle.mainloop()