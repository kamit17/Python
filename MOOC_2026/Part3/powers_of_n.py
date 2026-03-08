'''
Please change the program from the previous exercise so that the user gets to input also the base which is multiplied (in the previous program the base was always 2).
'''

upper_limit = int(input("Upper limit: "))
base = int(input("Base: "))
i = 1
while i <= upper_limit:
    print(i)
    i = i * base
    