#Write a program that computes the sum of the squares of the numbers in the list numbers.
#For example a call with,numbers = [2, 3, 4]shouldprint4+9+16 which is 29.

def sum_of_squares(xs):
    count = 0
    square = 0
    for i in xs:
        square = i ** 2
        count += square
    return count

#print(sum_of_squares([2,3,4]))

assert(sum_of_squares([2,3,4])== 29)
assert(sum_of_squares([ ]) == 0)
assert(sum_of_squares([2, -3, 4]) == 29)
