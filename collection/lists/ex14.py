# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

list1=[1,2,3,4,5,6,7,8]
list2=[]
for i in  list1:
    if i %2 != 0:
        list2.append(i)
        
print(list2)