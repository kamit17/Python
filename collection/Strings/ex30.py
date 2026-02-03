#30. Write a Python program to print the following floating numbers upto 2 decimal places
n = float(input('Enter the digit you want : '))

print("formatted number is : {:.2f}".format(n))
print("formatted number with sign is : {:+.2f}".format(n))
print("formatted number with sign is : {:.0f}".format(n))
