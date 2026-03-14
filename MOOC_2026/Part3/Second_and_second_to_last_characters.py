'''
Please write a program which asks the user for a string. The program then prints out a message based on whether the second character and the second to last character are the same or not. See the examples below.

'''
input_string = input("Please type in a string: ")
#print(input_string[1])
#print(input_string[-2])
if input_string[1] == input_string[-2]:
    print("The second and the second to last characters are ",input_string[1])
else:
    print("The second and the second to last characters are different")
