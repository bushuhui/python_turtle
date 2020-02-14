# encoding: utf-8

import turtle


def tree(plist, l, a, f, lev=5):
    """
    draw tree recursively

    plist is list of pens
    l is length of branch
    a is half of the angle between 2 branches
    f is factor by which branch is shortened from level to level.
    """

    if l > 5:
        lst = []

        for p in plist:
            if lev > 0:
                p.pensize(lev)
            else:
                p.pensize(1)

            # 沿着当前的方向画画
            # Move the turtle forward by the specified distance, in the direction the turtle is headed.
            p.forward(l)

            # Create and return a clone of the turtle with same position,
            # heading and turtle properties.
            q = p.clone()
            p.left(a)  # Turn turtle left by angle units

            # turn turtle right by angle units, nits are by default degrees,
            # but can be set via the degrees() and radians() functions.
            q.right(a)
            lst.append(p)  # 将元素增加到列表的最后
            lst.append(q)

        # draw sub-level tree
        tree(lst, l * f, a, f, lev*0.75)


def draw():
    p = turtle.Turtle()
    p.color("green")

    # Make the turtle invisible. It's a good idea
    # to do this while you're in the middle of doing some complex drawing,
    p.hideturtle()
    p.speed(0)

    p.left(90)  # Turn turtle left by angle units. direction 调整画笔

    # Move turtle to an absolute position. If the pen is down, draw line.
    # Do not change the turtle's orientation.
    # Pull the pen down – drawing when moving.
    # 这三条语句是一个组合相当于先把笔收起来再移动到指定位置，再把笔放下开始画
    # 否则turtle一移动就会自动的把线画出来
    p.penup()  # Pull the pen up – no drawing when moving.
    p.goto(0, -270)
    p.pendown()

    # draw tree
    tree([p], 270, 65, 0.6375, 20)


if __name__ == "__main__":
    draw()

    turtle.mainloop()
