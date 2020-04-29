#Triangle Geometry Functions - www.101computing.net/triangle-geometry-functions

#A function to calculate and return the perimeter of a triangle
def getPerimeter(a,b,c):
  perimeter = a + b + c
  return perimeter
  
  
#Main program starts here
side1 = int(input("Enter the length of the first side:"))
side2 = int(input("Enter the length of the second side:"))
side3 = int(input("Enter the length of the third side:"))

perimeter = getPerimeter(side1,side2,side3)

print("The perimeter of this triangle is " + str(perimeter))