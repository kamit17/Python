# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Go to the editor
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

s= ['Red','green','yellow','white','Black']
print(s[1:4])
# def remove(list1,pos):
#     newlist = []
    
#     #traverse the list
#     for x in range(len(list1)):
        
#         # if index not equal to pos
#         if x != pos:
#             newlist.append(list1[x])
#     print(newlist)
        
# # driver code 
# list1 = [10, 20, 30, 40, 50] 
# pos = 2
# remove(list1, pos) 