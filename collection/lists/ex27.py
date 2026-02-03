# 27. Write a Python program to find the second smallest number in a list.

# Take in the list
# Sort the elements in the list one by one
# print the last element of the list

list1 = [2,3,4,1,6,9,33,24,39,0]
for i in  range(len(list1)+1):
    list1.sort()
    
print('The second smallest value of the list is: ',list1[1])