import math
def f(r):
    """Return (circumference,area of a circle of radius r)"""
    c = 2 * math.pi * r
    a = math.pi * r * r
    return(c,a)

print(f(3.14))
