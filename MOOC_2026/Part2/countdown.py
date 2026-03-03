#Write a program that takes an integer and counts down to zero – print the value

number =int(input("Enter an integer: "))

print("entering the loop")
while number > 0:
    print(number)
    number -= 1
