temp_in_F=float(input("Enter temperature in Fahrenheit: "))
temp_in_C=(temp_in_F-32)*5/9
is_cold= temp_in_C<0

print(is_cold)
print(f"{temp_in_F} degrees Fahrenheit equals {temp_in_C} degrees Celsius.")
if is_cold:
    print("Brr! It's cold in here!.")
