#Lists can be used to represent mathematical vectors. In this exercise and several that follow you will write functions to perform standard operations on vectors. Create a script named vectors.py and write Python code to pass the tests in each case.

#Write a function add_vectors(u, v) that takes two lists of numbers of the same length, and returns a new list containing the sums of the corresponding elements of each:
from test_suite import test

def add_vectors(u,v):
    """ Function to add two vectors"""


    #sum = [u[0]+v[0],u[1]+v[1]]
    #iterate through rows
    result = []   #initialize a result variable to be an empty list
    for i in range(0,len(u)): #loop
        result.append(u[i] + v[i]) #create a new element and append it to result
    return (result)


test(add_vectors([1, 1], [1, 1]) == [2, 2])
test(add_vectors([1, 2], [1, 4]) == [2, 6])
test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])


