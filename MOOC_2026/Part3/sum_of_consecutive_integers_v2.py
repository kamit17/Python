'''
Please write a new version of the program in the previous exercise. In addition to the result it should also print out the calculation performed:
'''


limit = int(input("Limit:"))
number = 1
sum = 0
expression = ""
while sum <=limit:
    sum += number
    if expression == "":
        expression = f"{number}"
    else:
        expression = f"{expression} + {number}"
    number +=1
print(f"The consecutive sum: {expression} = {sum}")

