number = int(input("Please type in a number: "))
if number > 100:
    print("The number is greater than 100.")
    number = int(number) - 100
print(f"The number is now {number}.")