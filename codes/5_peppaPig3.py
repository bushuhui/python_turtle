import turtle as t


'''
https://blog.csdn.net/qq_14823403/article/details/81390575

t.pu()          提起画笔
t.pd()          移动时绘制图形，缺省时也为绘制
t.seth          设置当前朝向为angle角度
t.begin_fill()  准备开始填充图形
t.color         同时设置pencolor=color1, fillcolor=color2
t.goto          设置笔的坐标
t.circle(70,20) 半径 度数

colors:
15,124,215      乔治裤子颜色外面
66,163,242      乔治裤子颜色里面

134  196  247   天空的颜色
123,245,95      草地的颜色
253,6,6         鞋子外面
253,70,70       鞋子里面
130,119,100     泥坑
'''

# global settings
r_a = 0.8
wight = 1100
height = 700


def move_pen(x, y):
    t.pu()
    t.goto(x - wight / 2 + 50, y - height / 2 + 50)
    t.pd()


def pen_set(size, r1, g1, b1, r2=0, g2=0, b2=0):
    t.pensize(size)
    t.color((r1, g1, b1), (r2, g2, b2))


def draw_grid():
    pen_set(1, 0, 0, 0, 0, 0, 0)
    for i in range(20):
        move_pen(0 + i * 50, 0)
        t.seth(90)
        t.fd(600)
    for i in range(12):
        move_pen(0, 0 + i * 50)
        t.seth(0)
        t.fd(1000)


def draw_bg():
    # 画草地

    move_pen(0, 350)
    pen_set(4, 123, 245, 95, 123, 245, 95)
    t.begin_fill()
    t.seth(-90)
    t.fd(350)
    t.seth(0)
    t.fd(1000)
    t.seth(90)
    t.fd(350)
    t.end_fill()
    # 画天空
    move_pen(0, 350)
    pen_set(4, 134, 196, 247, 134, 196, 247)
    t.begin_fill()
    t.seth(90)
    t.fd(250)
    t.seth(0)
    t.fd(1000)
    t.seth(-90)
    t.fd(250)
    a = -180 + r_a
    for i in range(50):
        a = a - r_a / 50
        t.seth(a)
        t.fd(500 / 50)
    a = 180
    for i in range(50):
        a = a - r_a / 50
        t.seth(a)
        t.fd(500 / 50)
    t.end_fill()


def draw_mud_pit():
    # 画泥坑
    pen_set(5, 130, 119, 100, 130, 119, 100)
    move_pen(350, 150)
    t.begin_fill()
    t.seth(-180)
    t.circle(50, 125)
    t.seth(-20)
    t.circle(350, 60)
    t.seth(20)
    t.circle(50, 30)
    t.seth(10)
    t.circle(50, 30)
    t.seth(0)
    t.circle(50, 30)
    t.seth(40)
    t.circle(50, 90)
    t.seth(170)
    t.circle(500, 45)
    t.end_fill()


def draw_shoes():
    pen_set(3, 253, 6, 6, 253, 70, 70)
    move_pen(400, 100)
    t.begin_fill()
    t.seth(0)
    t.fd(50)
    t.seth(87)
    t.fd(50)
    t.seth(180)
    t.fd(25)
    t.seth(-93)
    t.fd(20)
    t.seth(-180)
    t.fd(25)
    t.seth(-120)
    t.circle(45, 38)
    t.end_fill()
    move_pen(470, 100)
    t.begin_fill()
    t.seth(0)
    t.fd(50)
    t.seth(87)
    t.fd(50)
    t.seth(180)
    t.fd(25)
    t.seth(-93)
    t.fd(20)
    t.seth(-180)
    t.fd(25)
    t.seth(-120)
    t.circle(45, 38)
    t.end_fill()


def draw_leg():
    pen_set(6, 255, 155, 192, 255, 155, 192)
    move_pen(440, 140)
    t.seth(90)
    t.fd(20)
    move_pen(510, 140)
    t.seth(90)
    t.fd(20)


def draw_trousers():
    move_pen(400, 300)
    pen_set(6, 15, 124, 215, 66, 163, 242)
    t.begin_fill()
    d_a = 100
    a = -130
    for i in range(60):
        a = a + 2
        t.seth(a)
        t.fd(3)
    for i in range(14):
        a = a + 0.02
        t.seth(a)
        t.fd(2)
    a = 0 - a
    for i in range(14):
        a = a + 0.02
        t.seth(a)
        t.fd(2)
    for i in range(60):
        a = a + 2.2
        t.seth(a)
        t.fd(3)
    t.end_fill()


def draw_tile():
    move_pen(550, 177)
    pen_set(6, 255, 155, 192, 255, 155, 192)
    a = -60
    for i in range(25):
        a = a + 4
        t.seth(a)
        t.fd(1)
    t.circle(5)
    a = -a
    for i in range(30):
        a = a + 4
        t.seth(a)
        t.fd(1)


def draw_hands():
    move_pen(550, 250)
    pen_set(6, 255, 155, 192, 255, 155, 192)
    t.seth(20)
    t.fd(70)
    move_pen(600, 270)
    t.seth(60)
    t.fd(20)
    move_pen(600, 270)
    t.seth(-20)
    t.fd(20)

    move_pen(380, 250)
    t.seth(160)
    t.fd(50)
    move_pen(350, 260)
    t.seth(100)
    t.fd(20)
    move_pen(350, 260)
    t.seth(-140)
    t.fd(20)


def draw_face():
    move_pen(400, 360)
    pen_set(4, 255, 155, 192, 255, 196, 218)
    t.begin_fill()
    a = -120
    for i in range(20):
        a = a + 2.5
        t.seth(a)
        t.fd(2.2)
    for i in range(130):
        a = a + 1.3
        t.seth(a)
        t.fd(1.8)
    for i in range(35):
        a = a + 1.4
        t.seth(a)
        t.fd(2)
    for i in range(50):
        a = a + 0.35
        t.seth(a)
        t.fd(2)
    for i in range(50):
        a = a + 0.2
        t.seth(a)
        t.fd(2)
    n = 0.4
    for i in range(180):
        if 0 <= i < 30 or 60 <= i < 90 or 120 <= i < 150:
            n = n + 0.08
            t.lt(3)  # 向左转3度
            t.fd(n)  # 向前走a的步长
        else:
            n = n - 0.08
            t.lt(3)
            t.fd(n)
    a = -50
    for i in range(20):
        a = a + 2.8
        t.seth(a)
        t.fd(5)
    t.end_fill()


def draw_other():
    move_pen(310, 440)
    pen_set(6, 255, 145, 192, 255, 145, 192)
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    move_pen(330, 430)
    t.begin_fill()
    t.circle(3)
    t.end_fill()

    pen_set(6, 255, 145, 192, 255, 255, 255)
    move_pen(410, 425)
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    move_pen(460, 395)
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    pen_set(6, 0, 0, 0, 0, 0, 0)
    move_pen(405, 429)
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    move_pen(455, 399)
    t.begin_fill()
    t.circle(3)
    t.end_fill()

    move_pen(510, 310)
    pen_set(6, 255, 155, 192, 255, 155, 192)
    t.begin_fill()
    t.circle(25)
    t.end_fill()

    move_pen(410, 340)
    pen_set(6, 255, 145, 192, 255, 145, 192)
    a = -80
    for i in range(20):
        a = a + 6
        t.seth(a)
        t.fd(3)
    move_pen(430, 445)
    pen_set(4, 255, 155, 192, 255, 196, 218)
    t.begin_fill()
    a = 120
    for i in range(40):
        a = a - 2
        t.seth(a)
        t.fd(1.2)
    a = -a
    for i in range(45):
        a = a - 2
        t.seth(a)
        t.fd(1.2)
    t.end_fill()
    move_pen(480, 430)
    t.begin_fill()
    a = 70
    for i in range(40):
        a = a - 1.5
        t.seth(a)
        t.fd(1.5)
    a = -80
    for i in range(45):
        a = a - 1.5
        t.seth(a)
        t.fd(1.5)
    t.end_fill()


def draw():
    # t.pensize(4)
    t.hideturtle()
    t.colormode(255)
    t.color((255, 155, 192), "pink")
    t.setup(wight, height)
    t.speed(10)

    draw_bg()
    draw_mud_pit()
    # draw_grid()
    draw_leg()
    draw_shoes()
    draw_trousers()
    draw_tile()
    draw_hands()
    draw_face()
    draw_other()


if __name__ == "__main__":
    draw()
    t.mainloop()
