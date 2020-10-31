#Lists can be used to represent mathematical vectors. In this exercise and several that follow you will write functions to perform standard operations on vectors. Create a script named vectors.py and write Python code to pass the tests in each case.

#Write a function add_vectors(u, v) that takes two lists of numbers of the same length, and returns a new list containing the sums of the corresponding elements of each:
from test_suite import test

def add_vectors(u,v):
    """ Function to add two vectors"""
    #print("What are the elements of the first vector")
    #c = []

    sum = [u[0]+v[0],u[1]+v[1]]

    return sum

test(add_vectors([1, 1], [1, 1]) == [2, 2])


