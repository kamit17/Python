# Write a function to sum up all the ven numbers in a list.

def even_sum(numbers):
    """prints sum of all even numbers in a list"""
    counter = 0
    for num in numbers:
        if num % 2 ==0 :
            counter = counter + num
    return counter

print(even_sum([2,3,4,5,6,7,8]))

