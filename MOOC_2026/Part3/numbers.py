'''Please write a program which asks the user for a number. The program then prints out all integer numbers greater than zero but smaller than the input.'''

upper_limit = int(input("Please type in a number: "))
number = 1
print("upper limit is", upper_limit)
while number < upper_limit:
    print(number)
    number += 1

