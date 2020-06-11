# Write a function that removes all occurrences of a given letter from a string:
# 
#     test(remove_letter("a", "apple") == "pple")
#     test(remove_letter("a", "banana") == "bnn")
#     test(remove_letter("z", "banana") == "banana")
#     test(remove_letter("i", "Mississippi") == "Msssspp")
#     test(remove_letter("b", "") = "")
#     test(remove_letter("b", "c") = "c")

from test_suite import test
def remove_letter(ltr, string):
    """Remove a letter ltr from a string.

    Removes all instances of ltr and returns a new string without it.
    """
    new_string = ""
    for char in string:
        if char != ltr:
            new_string = new_string + char
    return new_string

test(remove_letter("a", "apple") == "pple")
test(remove_letter("a", "banana") == "bnn")
test(remove_letter("z", "banana") == "banana")
test(remove_letter("i", "Mississippi") == "Msssspp")
# test(remove_letter("b", "") = "")
# test(remove_letter("b", "c") = "c")