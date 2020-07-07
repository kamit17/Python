"""
Write a Python program to get a string from a given string where all occurrences
of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""

string1 = input('Enter the string : ')
char = string1[0] #returns r
print(string1[1:]) #returns estart
string1 = string1.replace(char, '$')  #substituting $ in place of r
string1 = char + string1[1:] # r + esta$t
print(string1)
