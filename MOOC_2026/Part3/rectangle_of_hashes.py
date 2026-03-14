'''
Please modify the line_of_hashes.py so that it also asks for the height, and prints out a rectangle of hash characters accordingly.
'''


width = int(input("Enter the width of the string: "))
height = int(input("Enter the height of the rectangle: "))
row = 0

while row < height:
    print( width * '#')
    row += 1