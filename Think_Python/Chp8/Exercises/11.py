# Write a function that counts how many times a substring occurs in a string:
# Note : It does not work as expected. Need to research why the string.count method is not working
from test_suite import test

def count(substr,string):
    count = string.count(substr)

    return count

test(count("is", "Mississippi") == 2)
test(count("an", "banana") == 2)
test(count("ana", "banana") == 2)
test(count("nana", "banana") == 1)
test(count("nanan", "banana") == 0)
test(count("aaa", "aaaaaa") == 4)



