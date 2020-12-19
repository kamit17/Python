# Write a Python function that takes two lists and returns True if they have at least one common member. 

def common_data(list1,list2):
    
    result = False
    
    #traverse the first list
    for i in list1:
        
        #traverse the second list
        for j in list2:
            
            #check if common
            if i == j:
                result = True
                return result
            
#Driver code

a = [1,2,3,4,5,6]
b = [6,3,2,8,9,0]
print(common_data(a,b))