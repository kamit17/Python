import math

def distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def area2(xc,yc,xp,yp):
    radius = distance(xc,yc,xp,yp)
    result = aread(radius)
    return result