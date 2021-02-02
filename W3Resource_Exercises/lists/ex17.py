# Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).

list1 = list()
for i in range (1,30):
    list1.append(i**2)
#print(list1[:5])
print(list1[5:])