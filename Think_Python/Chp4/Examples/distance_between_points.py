def distance(x1,y1,x2,y2):
    """ Program to  find distance between 2 points  given by the coordinates using Pythagorean theorem
         sqrt((x2-x1)**2  + (y2-y1)**2).
    """
    dx = x2-x1
    dy = y2 - y1
    dsquared = dx + dx + dy + dy
    result = dsquared**0.5
    return result   # returns a float value

print(distance(1,2,4,6))