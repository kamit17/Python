"""
8. Write a program which, given the length of three sides of a triangle, will determine whether
the triangle is right- angled. Assume that the third argument to the function is always the
longest side. It will return True if the triangle is right-angled, or False otherwise.

"""

def is_rightangled(a, b, c):
    return abs(a **2 + b**2 - c**2) < 0.1

x = float(input("Enter the length of side side :  "))
y = float(input("Enter the length of the base :  "))
z = float(input("Enter the length of the Hypotenuse :  "))
print('Is the triangle  rightangled ? : ', is_rightangled(x,y,z))
