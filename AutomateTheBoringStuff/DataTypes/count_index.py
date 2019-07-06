# Python code to demonstrate teh workin of index() and count()

# initializing list
list1 = [2, 1, 3, 5, 4, 3, 8]

# using index() to print first occurencene of 3
print('The first occurence of  3 after 3rd position is : ', end='')
print(list1.index(3, 3, 6))

# using count to count number of occurences of 3
print('The number of occurences of 3 is : ', end='')
print(list1.count(3))


# using del to delete elements from pos2 to 5
del list1[2:5]

# displaying list after deleting
print("list elements after deleting are : ", end='')
for i in range(0, len(list1)):
    print(list1[i], end=' ')

print('\r')

# using pop() to delete element at pos 2
list1.pop(2)

# displaying list after poopping
#print("list elements after pop are :",end = '')
# for i in range(0,len(list1)):
#print(list1[i],end = '.')

# displaying list after popping
print("List elements after popping are : ", end="")
for i in range(0, len(list1)):
    print(list1[i], end=" ")
