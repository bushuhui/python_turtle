import turtle as t

t.setup(800, 600)
t.pen(shown=False, pendown=False, pensize=10, speed=0)

colorlist = [(255, 0, 0), (255, 165, 0), (255, 255, 0), \
             (0, 255, 0), (0, 255, 255), (0, 0, 255), (139, 0, 255)]
colorlist.reverse()

t.fd(-250)
t.seth(-40)

t.colormode(255)

t.pendown()
for color in colorlist [:-1]:
    t.pencolor(color)
    t.circle(30, 80)
    t.circle(-30, 80)

t.pencolor(colorlist [-1])
t.circle(30, 80 / 2)
t.fd(40)
t.circle(25, 180)
t.fd(40 * 2 / 3)

t.mainloop()