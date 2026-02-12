'''
Please write a program which asks the user for a floating point number and then prints out the integer part and the decimal part separately. Use the Python int function.
'''

number = float(input("Enter a number greater than 0: "))

print(f"Integer part: {int(number)} \n Decimal part: {round (number - int(number),2)}")