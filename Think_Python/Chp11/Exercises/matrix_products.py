# Write a function dot_product(u, v) that takes two lists of numbers of the same length, and returns the sum of the products of the corresponding elements of each (the dot_product).

from test_suite import test

def dot_product(a,b):
    """ Function to add two vectors"""
    product = 0
    for i in range(0,len(a)):
        product = product + a[i] * b[i]
    return product

test(dot_product([1, 1], [1, 1]) ==  2)
test(dot_product([1, 2], [1, 4]) ==  9)
test(dot_product([1, 2, 1], [1, 4, 3]) == 12)