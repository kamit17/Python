# Write a function area_of_circle(r) which returns the area of a
# circle of radius r.
import math
def area_circle(r):
    """
        Calculates the area of a circle of radius r
    """
    area = 3.14 * r ** 2
    
    return area

print( area_circle(5))