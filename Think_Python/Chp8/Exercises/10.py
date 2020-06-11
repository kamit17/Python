# Write a function that recognizes palindromes. (Hint: use your reverse function to make this easy!):
# 
#     test(is_palindrome("abba"))
#     test(not is_palindrome("abab"))
#     test(is_palindrome("tenet"))
#     test(not is_palindrome("banana"))
#     test(is_palindrome("straw warts"))
#     test(is_palindrome("a"))
#     # test(is_palindrome(""))    # Is an empty string a palindrome?
#

from test_suite import test
from seven import reverse

# def reverse(test_string):
#     test_string = test_string[::-1]
#     return test_string

def is_palindrome(a_string):
    """Function that recognizes palindrome"""
    return a_string == reverse(a_string)


test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))
#test(is_palindrome(""))    # Is an empty string a palindrome?   