# Python code to demonstarate copy operation

# importing "copy for copy Operations"
import copy

# initializing list 1
list1 = [1, 2, [3, 5], 4]

# using deepcopy to deep copy
list2 = copy.deepcopy(list1)

# original elements of the list
print("the original elements before deepcopy")
for i in range(0, len(list1)):
    print(list1[i], end=' ')

print("\r")

# adding an element to the new list
list2[2][0] = 7

# checking if the change is being reflected
print('The new list of element after deep copy')
for i in range(0, len(list2)):
    print(list2[i], end=' ')

print('\r')

# change not being reflected in Original list
# as it is deep copy

print('The original elements after deep copy are :')
for i in range(0, len(list1)):
    print(list1[i], end=' ')
