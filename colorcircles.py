from turtle import *
from random import randint

speed(0)

r = 50
for j in range(1):
    for i in range(18):
        col = i % 5 + 1  # randint(1, 5)
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
        circle(r)
        left(20)

    r += 10

done()