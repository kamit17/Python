'''
Please write a program which asks the user for a string and then prints it out so that exactly 20 characters are displayed. If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.

You may assume the input string is at most 20 characters long.

Please type in a string: python

**************python
'''


'''
Total desired = 20
Input takes upto = len(input_string)
Starts needed = 20 - len(input_string)
'''
input_string = input("Please type in a string: ")

padding_needed = 20 - len(input_string)
padding = ""
index = 0

while index < padding_needed:
    padding +="*"
    index +=1
print(padding + input_string)


