#Write a program that computes the sum of the squares of the numbers in the list numbers.
#For example a call with,numbers = [2, 3, 4]shouldprint4+9+16 which is 29.

def square_sum(lis):
    count = 0
    square = 0
    for i in lis:
        square = i ** 2
        count += square
    return count
print(square_sum([2,3,4]))
        
        