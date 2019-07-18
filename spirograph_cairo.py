import cairo
import math

#Definitions
filename = 'spirograph-simple.png'
WIDTH = 1000
HEIGHT = 1000
a = 400
b = 275
d = 225

def create_image(width, height):
    global surface
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    cr = cairo.Context(surface)
    cr.set_source_rgb(1, 1, 1)
    cr.rectangle(0, 0, width, height)
    cr.fill()
    return cr

def save_image(filename):
    global surface
    surface.write_to_png(filename)

def create_spiro(a, b, d):
    dt = 0.01
    t = 0
    pts = []
    while t < 2*math.pi*b/math.gcd(a, b):
        t += dt
        x = (a - b) * math.cos(t) + d * math.cos((a - b)/b * t)
        y = (a - b) * math.sin(t) - d * math.sin((a - b)/b * t)
        pts.append((x, y))
    return pts

def polygon(cr, pts):
    if pts:
        cr.move_to(pts[0][0], pts[0][1])
        for x, y in pts[1:]:
            cr.line_to(x, y)

#Open the image
cr = create_image(WIDTH, HEIGHT)
cr.translate(WIDTH/2, HEIGHT/2)

#Draw the curve
cr.set_line_width(5)
cr.set_source_rgb(1, 0, 0)
pts = create_spiro(a, b, d)
polygon(cr, pts)
cr.stroke()

#Save the image
save_image(filename)