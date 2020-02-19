
# coding:utf-8
import turtle as t
import time


'''
    作者：通信1702 刘传现
    学号：41724279
    功能：画一个派大星和心形图案，并且使心形图案动起来
    日期：2019/3/15
    
    https://www.jianshu.com/p/81a307f0d7df
'''


# 画派大星肢体的一只
def drawLag():
    t.left(10)
    t.pendown()
    t.fd(160)  # 臂长
    t.circle(30, 155)  # 手末端
    t.fd(160)


# 画半片叶子
def drawLeaf():
    t.pencolor('#CC6699')
    t.fillcolor('#CC6699')
    t.begin_fill()
    t.circle(50, 36)  # 1
    t.left(95)
    t.fd(22)  # 2
    t.right(140)
    t.fd(22)  # 3
    t.left(70)
    t.circle(50, 72)  # 4
    t.left(70)
    t.fd(22)  # 5
    t.right(140)
    t.fd(22)  # 6
    t.left(70)
    t.circle(30, 50)
    t.left(100)
    t.right(12)
    t.forward(105)
    t.end_fill()


# 画心形
def drawHeart(r, c):
    t.pendown()
    t.down()
    t.fillcolor(c)
    t.begin_fill()
    factor = 180
    t.seth(45)
    t.circle(-r, factor)
    t.fd(2 * r)
    t.right(90)
    t.fd(2 * r)
    t.circle(-r, factor)
    t.end_fill()
    t.penup()


def drawEye(a, b):
    t.speed(0)
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + b
            t.lt(3)  # 向左转3度
            t.fd(a)  # 向前走a步长
        else:
            a = a - b
            t.lt(3)
            t.fd(a)


# 画派大星
def drawPatrickStar():
    # 画派大星的五角星
    t.penup()
    t.forward(300)
    t.left(50)
    t.fillcolor('#FF9966')
    t.begin_fill()
    for i in range(5):
        drawLag()
        t.right(93)
    t.end_fill()

    # 画裤腰带和肚脐
    t.fillcolor('yellow')
    t.begin_fill()
    t.penup()
    t.right(195)
    t.forward(215)
    t.pendown()
    t.circle(1300, -4.85)
    t.left(180)
    t.circle(5)  # 肚脐
    t.left(180)
    t.circle(1300, -4.85)
    t.left(115)
    t.forward(20)
    t.right(115)
    t.circle(1500, 9)
    t.right(120)
    t.forward(20)
    t.end_fill()

    # 画裤子
    t.fillcolor('yellow')
    t.begin_fill()
    t.penup()
    t.left(180)
    t.forward(100)
    t.pendown()
    t.left(100)  # 左边裤腿
    t.forward(90)
    t.left(60)
    t.forward(60)  #
    t.right(50)
    t.forward(50)  # 裤裆
    t.right(40)
    t.forward(60)  #
    t.left(60)
    t.forward(90)  # 右边裤腿
    t.left(98)
    t.forward(88)  #
    t.left(68)
    t.forward(240)  #
    t.end_fill()

    # 画裤子上的第一片叶子
    t.penup()
    t.left(65)
    t.forward(35)
    t.fillcolor('#CC6699')
    t.begin_fill()
    t.pendown()
    t.forward(45)  # 1
    t.left(98)
    t.forward(35)  # 2
    t.pencolor('yellow')
    t.left(60)
    t.forward(50)  # 3
    t.left(120)
    t.forward(30)  # 4
    t.left(70)
    t.forward(20)  # 5
    t.right(150)
    t.forward(20)  # 6
    t.left(75)
    t.forward(15)
    t.end_fill()

    # 第二片，大叶子
    t.penup()
    t.right(141)
    t.fd(90)
    t.right(108)
    drawLeaf()

    # 第三片叶子
    t.penup()
    t.left(150)
    t.fd(183)
    t.pendown()
    t.left(45)
    t.fillcolor('#CC6699')
    t.begin_fill()
    t.pencolor('black')
    t.fd(50)  # 1
    t.left(100)
    t.fd(30)  # 2
    t.left(30)
    t.pencolor('#CC6699')
    t.fd(45)  # 3
    t.left(90)
    t.fd(25)  # 4
    t.left(80)
    t.fd(30)  # 5
    t.right(150)
    t.fd(30)  # 6
    t.left(110)
    t.fd(40)
    t.end_fill()

    # 画眉毛
    t.penup()
    t.right(168)
    t.fd(375)  # 到画眉毛的起笔处
    t.right(90)

    t.pensize(5)  # 左眉毛
    t.pendown()
    t.pencolor('black')
    t.fd(20)

    t.penup()  # 右眉毛
    t.fd(20)
    t.pendown()
    t.right(40)
    t.fd(20)

    # 画眼框
    t.penup()  # 右眼
    t.right(145)
    t.fd(20)
    t.pensize(2)
    t.pendown()
    t.fillcolor('white')
    t.begin_fill()
    t.pencolor('black')
    drawEye(0.3, 0.05)
    t.end_fill()

    t.penup()  # 左眼
    t.fd(30)
    t.right(90)
    t.fd(5)
    t.left(90)
    t.pendown()
    t.fillcolor('white')
    t.begin_fill()
    t.pencolor('black')
    drawEye(0.3, 0.05)
    t.end_fill()

    # 画眼珠
    t.penup()  # 左眼
    t.left(110)
    t.fd(14)
    t.pendown()
    t.right(100)
    t.fillcolor('black')
    t.begin_fill()
    drawEye(0.1, 0.02)
    t.end_fill()

    t.penup()  # 右眼
    t.left(180)
    t.fd(20)
    t.right(90)
    t.fd(25)
    t.left(90)
    t.pendown()
    t.fillcolor('black')
    t.begin_fill()
    drawEye(0.1, 0.02)
    t.end_fill()

    # 画嘴
    t.penup()
    t.right(180)
    t.fd(60)
    t.pendown()
    t.left(110)
    t.circle(60, 90)


# 画心
def hearts():
    drawHeart(20, 'pink')
    t.left(90)
    t.fd(50)
    drawHeart(10, 'pink')
    t.right(180)
    t.fd(50)
    drawHeart(15, 'blue')
    t.left(90)
    t.fd(50)
    drawHeart(10, 'blue')


def draw():
    t.tracer(False)

    # 设置画布

    t.pensize(3)

    t.screensize(bg='#293047')

    # 让心形动起来
    for z in range(10):
        t.reset()
        t.hideturtle()
        t.speed(0)
        drawPatrickStar()
        t.penup()
        t.goto(-50, 200 + z * 5)

        if z % 2 == 0:
            t.left(90)
            t.fd(30)
        else:
            t.right(90)
            t.fd(30)
        t.pendown()
        hearts()
        t.update()
        time.sleep(0.5)

    # 写署名
    t.pencolor('white')
    t.goto(-150, -250)
    t.write('By 海绵宝宝~~ ', font=('gungsuh', 20,), align="center", move=True)


if __name__ == '__main__':
    draw()
    t.mainloop()
