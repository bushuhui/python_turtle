
import turtle

def draw():
    """
    Moroccan Mosaic using Python Turtle - www.101computing.net/morroccan-mosaic/

    Ref:
        https://www.101computing.net/moroccan-mosaic/

    :return:
    """

    myPen = turtle.Turtle()
    myPen.shape("arrow")
    myPen.speed(1000)  # Set the speed of the turtle


    # A Procedue to draw a mosaic by repeating and rotating a polygon shape.
    def drawMosaic(color, numberOfSides, size, numberOfIterations):
        myPen.color(color)
        for i in range(0, numberOfIterations):
            for j in range(0, numberOfSides):
                myPen.forward(size)
                myPen.left(360 / numberOfSides)
            myPen.left(360 / numberOfIterations)


    mt = 2
    if (mt == 1):
        # Mosaic #1
        drawMosaic("#0B5CCB", 6, 100, 20)
    elif (mt == 2):
        # Mosaic #2
        drawMosaic("#CB0B3F",5,100,10)
    elif (mt == 3):
        # Mosaic #3
        drawMosaic("#0BCB9D",6,100,6)
    elif (mt == 4):
        # Mosaic #4
        drawMosaic("#FF5733",6,100,15)

    myPen.hideturtle()


if __name__ == "__main__":
    draw()
    turtle.done()
