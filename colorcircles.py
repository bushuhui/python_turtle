from turtle import *
from random import randint

speed(100)
for i in range(20):
    col = randint(1, 5)
    if col == 1:
        pencolor("orange")
    elif col == 2:
        pencolor("blue")
    elif col == 3:
        pencolor("green")
    elif col == 4:
        pencolor("purple")
    elif col == 5:
        pencolor("dark blue")
    circle(50)
    left(20)

done()