# Write a Python program to generate a 3*4*6 3D array whose each element is *.
#A 3D list is a list of lists containing lists with the innermost lists holding the 3D lists's values.
import pprint
pprint.pprint([[['*' for col in range(6)] for col in range(4)]for row in range(3)])