# Write a Python program to get unique values from a list

list1 = [100, 75, 100, 20, 75, 12, 75, 25]
empty_list1 = []

for i in list1:
    if i not in empty_list1:
        empty_list1.append(i)
        
print(empty_list1)