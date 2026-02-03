#22.Write a Python program to sort a string lexicographically.

# def lexographic(str1):
#
#     #Split str1 till where space is found.
#     words = str1.split()
#
#     #sort the string using sort
#
#     words.sort()
#
#     #iterate through words to print the words in alphabetical order
#     for i in words:
#         print(i)
# string1  = 'hello this is an example to sort in alphabetical order'
# #lexographic(string1)
# lexographic("hello")
#
def lexicographi_sort(s):
    return sorted(sorted(s),key=str.upper)
print(lexicographi_sort('Hello'))
