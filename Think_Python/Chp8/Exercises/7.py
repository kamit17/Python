# write a function that reverses its string argument and satisfies these tests
# test(reverse("happy") == "yppah")
# test(reverse("Python") == "nohtyP")
# test(reverse("") == "")
# test(reverse("a") == "a")
from test_suite import test

def reverse(test_string):
    test_string = test_string[::-1]
    return test_string

test(reverse("happy") == "yppah")
test(reverse("Python") == "nohtyP")
test(reverse("") == "")
test(reverse("a") == "a")