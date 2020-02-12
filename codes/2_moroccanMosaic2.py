import turtle

def draw():
    """
    Moroccan Mosaic using Python Turtle - www.101computing.net/morroccan-mosaic/

    :return:
    """

    myPen = turtle.Turtle()
    myPen.shape("arrow")
    myPen.speed(1000)  # Set the speed of the turtle


    # A Procedue to draw a mosaic by repeating and rotating a polygon shape.
    def drawMosaic(color1, numberOfSides1, size1, color2, numberOfSides2, size2, numberOfIterations):
        for i in range(0, numberOfIterations):
            myPen.color(color1)
            for j in range(0, numberOfSides1):
                myPen.forward(size1)
                myPen.left(360 / numberOfSides1)
            myPen.color(color2)
            for k in range(0, numberOfSides2):
                myPen.forward(size2)
                myPen.left(360 / numberOfSides2)

            myPen.left(360 / numberOfIterations)

    # Main Program Starts Here
    mt = 2
    if (mt == 1):
        # Mosaic 1: Hexagon and pentagon
        drawMosaic("blue",6,100,"lightblue",5,80,8)
    elif (mt == 2):
        # Mosaic 2: Octogons of different sizes
        drawMosaic("#980C6B", 8, 80, "#DD6BB8", 5, 70, 20)

    myPen.hideturtle()


if __name__ == "__main__":
    draw()
    turtle.done()