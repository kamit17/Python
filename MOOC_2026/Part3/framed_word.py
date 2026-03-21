'''
Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre. The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.

Word: testing

******************************
*          testing           *
******************************

line2 breakdown

*  +  11 spaces  +  testing  +  10 spaces  +  *  

'''

input_string = input("Type in a word: ")

padding_total = 30 -2 -len(input_string)
left_padding = padding_total //2
right_padding = padding_total - left_padding
line2="*" + " " *left_padding + input_string + " "* right_padding + "*"
print("*" *30)

print(line2)
print("*" *30)