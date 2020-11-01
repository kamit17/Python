# Write a function dot_product(u, v) that takes two lists of numbers of the same length, and returns the sum of the products of the corresponding elements of each (the dot_product).

from test_suite import test

def scalar_mult(s,v):
    product = []
    for i in range(0,len(v)):
       product.append(s * v[i])
    return product
    
test(scalar_mult(5, [1, 2]) == [5, 10])
test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])


def dot_product(a,b):
    """ Function to add two vectors"""
    product = 0
    for i in range(0,len(a)):
        product = product + a[i] * b[i]
    return product

test(dot_product([1, 1], [1, 1]) ==  2)
test(dot_product([1, 2], [1, 4]) ==  9)
test(dot_product([1, 2, 1], [1, 4, 3]) == 12)


def cross_product(a,b):
    cross_p=[]
    #for i in range(0, 3):
    cross_p.append(a[1] * b[2] - a[2]*b[1])
    cross_p.append(a[2]* b[0] - a[0] * b[2])
    cross_p.append(a[0] * b[1] - a[1] * b[0])
    return(cross_p)

test(cross_product([3,-5,4],[2,6,5])==[-49, -7, 28])


