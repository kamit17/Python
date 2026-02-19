'''
Please write a program which asks the user for three ltrs. The program should then print out whichever of the three ltrs would be in the middle if the ltrs were in alphabetical order.

You may assume the ltrs will be either all uppercase, or all lowercase.

Some examples of expected behaviour:

Sample output
1st ltr: x
2nd ltr: c
3rd ltr: p
The ltr in the middle is p

Sample output
1st ltr: C
2nd ltr: B
3rd ltr: A
The ltr in the middle is B
'''
ltr1 = input("1st ltr: ")
ltr2 = input("2nd ltr: ")
ltr3 = input("3rd ltr: ")

if ltr1 > ltr2:
    if ltr1 < ltr3:
        print(f"The letter in the middle is {ltr1}")
    elif ltr2 > ltr3:
        print(f"The letter in the middle is {ltr2}")
    else:
        print(f"THe letter in the middle is {ltr3}")
else:
    if ltr1 > ltr3:
        print(f"THe letter in the middle is {ltr1}")
    elif ltr2 < ltr3:
        print(f"The letter in the middle is {ltr2}")
    else:
        print(f"The letter in the middle is {ltr3}")



'''
if (ltr1 > ltr2 and ltr1 < ltr3) or (ltr1 < ltr2 and ltr1 > ltr3):
    print(ltr1)
elif (ltr2 > ltr1 and ltr2 < ltr3) or (ltr2 < ltr1 and ltr2 > ltr3):
    print(ltr2)
else:
    print(ltr3)
'''
