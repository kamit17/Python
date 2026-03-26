'''
Please write a program which asks the user to input a string. The program then prints out different messages if the string contains any of the vowels a, e or o.

You may assume the input will be in lowercase entirely. Have a look at the examples below.

'''

input_string = "hello there"

vowels = "aeiou"
for vowel in "aeiou":
    if vowel in input_string:
        print(f"{vowel} is there")
    else:
        print(f"{vowel} is not there")