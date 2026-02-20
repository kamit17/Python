value_gift = int(input("Value of gift:"))
tax = 0
if value_gift < 5000:
    print("No tax!")
elif  value_gift < 25000:
    tax = (100 + (value_gift - 5000) * 0.08)
    print(f"Amount of tax: {tax} euros")
elif value_gift <55000:
    tax = (1700 + (value_gift-25000) * 0.10)
    print(f"Amount of tax: {tax} euros")
elif value_gift  <200000:
    tax = (4700 + (value_gift-55000) * 0.12)
    print(f"Amount of tax: {tax} euros")
elif value_gift < 1000000:
    tax = 22100 + (value_gift - 200000) * 0.15
    print(f"Amount of tax: {tax:.1f} euros")
else:
    tax = 142100 + (value_gift - 1000000) * 0.17
    print(f"Amount of tax: {tax:.1f} euros")
    