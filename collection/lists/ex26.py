# 26. Write a python program to check whether two lists are circularly identical.
# A circular list is a special case of a linked list. It is a list where the endpoints are connected. That is, the last node in the list points back to the first node. 

# Using Python’s inbuilt function map() we can do this in one single step, where we have to map list2 in a string and then see if it exists in the mapping of twice of list1 (2*list1) in another string.
# python program to check if two  
# lists are circularly identical 
# using map function  
  
# function to check circularly identical or not 
def circularly_identical(list1, list2): 
     
    return(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2))) 
      
  
# driver code 
list1 = [10, 10, 0, 0, 10] 
list2 = [10, 10, 10, 0, 0] 
list3 = [1, 10, 10, 0, 0] 
  
  
# check for list 1 and list 2  
if (circularly_identical(list1, list2)): 
    print("Yes") 
else: 
    print("No") 
  
# check for list 2 and list 3  
if(circularly_identical(list2, list3)): 
    print ("Yes")  
else: 
    print ("No")  
