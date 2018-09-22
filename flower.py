# https://trinket.io/python/8c5713a987

from turtle import *

def regularShape(length,sides,angle):
  for i in range(sides):
    forward(length)
    left(angle)
    
def square(length):
  regularShape(length,4,90)

def slowArc(radius,segmentAngle,steps):
  sides = steps
  angle = 360/steps
  length = 2*3.142*radius/steps
  regularShape(length,sides,angle)

def arc360(radius,segmentAngle):
  slowArc(radius,segmentAngle,segmentAngle)

def slowCircle(radius,steps):
  slowArc(radius, 360, steps)
  
def circle360(radius):
  slowArc(radius, 360, 360)

def rectangle(base,height):
  for i in range(2):
    forward(base)
    right(90)
    forward(height)
    right(90)

def leaf(scale):
  length=0.6*scale
  left(45)
  forward(length)
  right(45)
  forward(length)
  right(135)
  forward(length)
  right(45)
  forward(length)
  right(180)
  
def moveAround(relX,relY,back):
  if back:
    relX = -1 * relX
    relY = -1 * relY
  forward(relX)
  right(90)
  forward(relY)
  left(90)

def stem(base,height,col):
  color(col)
  pendown()
  begin_fill()
  rectangle(base,height)
  moveAround(base,height*0.7,False)
  leaf(0.5*height)
  moveAround(base,height*0.7,True)
  end_fill()
  penup()

def filledCircle(radius,col):
  color(col)
  pendown()
  begin_fill()
  circle(radius)
  end_fill()
  penup()


def petals(radius,bloomDiameter,noOfPetals,col):
  penup()
  color(col)
  petalFromEye=1.5*radius
  relY = (radius+petalFromEye)/2
  relX = petalFromEye/2
  angle=360/noOfPetals
  moveAround(relX,relY,False)
  for i in range(noOfPetals):
    pendown()
    begin_fill()
    circle(radius)
    end_fill()
    penup()
    left((i+1)*angle)
    forward(petalFromEye)
    right((i+1)*angle)
  moveAround(relX,relY,True)

def bloom(relX,bloomDiameter,colPetal,colEye):
  smallRadius=bloomDiameter/5
  penup()
  forward(relX)
  petals(smallRadius,bloomDiameter,6,colPetal)
  filledCircle(smallRadius,colEye)
  forward(-relX)

def flower(height):
  stem(10,0.6*height,"green")
  bloom(5,0.8*height,"white","yellow")
  
# main program starts here

speed(500)

penup()
goto (-160,0)
pendown()
color("blue")
square(50)

penup()
goto (0,0)
pendown()
flower(250)

penup()
goto (160,0)
pendown()
color("magenta")
circle360(35)

color("red")
slowCircle(30,36)

color("orange")
slowCircle(25,16)

color("blue")
slowCircle(20,8)

hideturtle()



