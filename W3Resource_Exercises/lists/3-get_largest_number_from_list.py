# Write a Python program to get the largest number from a list


def largest_number(items):
    
    max = items[0]
    for i in items:
        if i > max:
            max = i
            
    return max
    
print(largest_number([1,2,10,7887,1231231]))