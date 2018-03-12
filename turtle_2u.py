from turtle import *

speed(20)

color('red', 'green')
# goto(100, 0)
begin_fill()
while True:
    forward(300)
    left(175)
    if abs(pos()) < 1:
        break
end_fill()

goto(-500, 0)
color('yellow', 'blue')
begin_fill()
for i in range(100):
    forward(200)
    left(175)
    if abs(pos()) < 1:
        break
end_fill()
done()
