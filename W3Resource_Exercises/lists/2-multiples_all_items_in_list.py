# Write a Python program to multiply all the items in a list.


def multiply(list_items):
    
    product = 1
    for i in list_items:
        product = product * i
    return product

print(multiply([1,2,-8]))