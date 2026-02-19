age = int(input("What is your age?"))

if age >0 and age <= 5:
    message = "I suspect you can't write quite yet"
elif age >5:
    message = f"Ok, you're {age} years old"
else:
    message ="That must be a mistake"
print(message)