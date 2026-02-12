number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")

if operation == "add":
    result = number1 + number2
    print(f"The result is: {result}")
if operation == "subtract":
    result = number1 - number2
    print(f"The result is: {result}")
if operation == "multiply":
    result = number1 * number2
    print(f"The result is: {result}")
if operation == "divide":
    if number2 != 0:
        result = number1 / number2
        print(f"The result is: {result}")
    else:
        print("Error: Division by zero is not allowed.")