#Sum up all the negative numbers in a list.

def sum_negative(numbers):
    """Prints the sum of negative numbers in a list"""
    counter = 0
    for num in numbers:
        if num % 2!= 0:
            counter += num
    return counter
print(sum_negative([3,3,5,10]))

