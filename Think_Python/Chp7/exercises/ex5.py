#5. Sum all the elements in a list up to but not including the first even number.
#(What if there is no even number?)
#numbers =[10,20,30,15,11,,25,22,31,999]
import random

def sum_of_initial_odds(lst):
    sum = 0
    for i in lst:
        if i % 2 !=0:
            sum = sum + i
        else:
            break
    return sum


print (sum_of_initial_odds([17,27,33,10,20,30,15,11,17,25,22,31,999]))


print (sum_of_initial_odds([1,3,1,4,3,8]) )
# print (sum_of_initial_odds([6,1,3,5,7]))# == 0
# print sum_of_initial_odds([1, -7, 10, 23]) == -6
# print sum_of_initial_odds(range(1,555,2)) == 76729