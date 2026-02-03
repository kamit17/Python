#Python program to get the difference between two lists

list1 = [1,2,3,4,5,6]
list2=[2,3,4,11,15]
list_diff=[]
# for i in list1 + list2:
#     if i not in list1 or i not in list2:
#         list_diff.append(i)
list_diff=[i for i in list1 + list2 if i not in list1 or i not in list2]
print(list_diff)        