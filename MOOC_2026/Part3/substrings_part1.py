
'''
Please write a program which asks the user to type in a string. The program then prints out all the substrings which begin with the first character, from the shortest to the longest. Have a look at the example below.
'''

input_string = input("Please type in a string: ")
for i in range(len(input_string)):
    print(input_string[0:i+1])
#print(input_string[0])
#print(input_string[0:2])
#print(input_string[0:3])
#print(input_string[0:4])
