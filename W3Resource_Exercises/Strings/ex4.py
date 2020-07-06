"""
Write a Python program to get a string from a given string where all occurrences
of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""

string1 = input('Enter the string : ')
char = string1[0]
print(string1[1:])
string1 = string1.replace(char, '$')
string1 = char + string1[1:]
print(string1)
