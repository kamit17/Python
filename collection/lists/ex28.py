# Write a Python program to find the second largest number in a list.

list1 = [2,3,4,1,6,9,33,24,39,0]
n = len(list1)
for i in  range(n+1):
    list1.sort()
print(list1)
    
print('The second larget value of the list is: ',list1[n-2])