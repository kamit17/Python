# Write a function that mirrors its argument:
#  test(mirror("good") == "gooddoog")
#     test(mirror("Python") == "PythonnohtyP")
#     test(mirror("") == "")
#     test(mirror("a") == "aa")
#

from test_suite import test

def mirror(test_string):
    test_string = test_string+test_string[::-1]
    return test_string

test(mirror("Python") == "PythonnohtyP")
test(mirror("") == "")
test(mirror("a") == "aa")