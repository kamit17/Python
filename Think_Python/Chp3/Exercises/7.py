"""
Write a program which, given the length of two sides of a right-angled triangle, returns the
length of the hypotenuse.(Hint:x ** 0.5 will return the squareroot.)
a**2 + b**2 = c**2
"""
def  triangle (a, b):
    c = (a**2 + b**2) ** 0.5
    return c

x = int(input("Enter the length of side side :  "))
y = int(input("Enter the length of the base :  "))

print('The length of the hypotenus is: ', triangle(x,y))