# Write a function to count how many odd numbers are in a list.

def odd_nums_in_list(xs):
    counter = 0
    for i in xs:
        if i % 2 == 1:
            counter +=1
        return counter
    
assert odd_nums_in_list([]) == 0
assert odd_nums_in_list([1]) == 1
assert odd_nums_in_list([-1]) == 1
assert odd_nums_in_list([0]) == 0
assert odd_nums_in_list([1, 7, -3]) == 3
assert odd_nums_in_list([1, 2, 3, 4, 5]) == 3
        