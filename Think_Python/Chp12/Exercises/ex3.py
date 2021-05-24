#copy module
#In python, assignment statements do not copy objects. They create bindings between a target and an object.

# A copy is sometimes needed so one can change one copy without changing the other.

#importing copy module
import copy

#initializing list
li1=[1,2,[3,5],4]

#using copy for shallow copy
#lis2=copy.copy(li1)

#using deep copy for deepcopy
#li3=copy.deepcopy(li3)


# Deep copy -- Copying occurs recursively . It means first constructing  a new collection object and then recursively populating it with copies of the child objects found in the original . 

#using deepcopy to deep copy

li2 = copy.deepcopy(li1)

#original elements of list
print("the original elements before deep copying:")
for i in range(0,len(li1)):
    print(li1[i],end=' ')
    
print('\r')

#adding an element to new list
li2[2][0] = 7

#change is reflected in l2
print("The new list of elements after deep copying:")
for i in range(0,len(li1)):
    print(li2[i],end=" ")

print("\r")

#change is not reflected in the original list
print('The original elements after deep copying')
for i in range(0,len(li1)):
    print(li1[i],end=" ")
print("\r")
#shallow copy  - constructing a new collection object and then populating it with references to the child objects found in the original .THe copying process does not recurse and therefore won't create copies of the child objects. Here, only a reference of object is copied in other object.
print('****Shallow copy*****')
li3=copy.copy(li1)

print("The original elements before shallow copying")
for i in range(0,len(li1)):
    print(li1[i],end=' ')
    
print("\r")

#adding an element to the new list
li3[2][0] = 11

#check if change is reflected
print("The original elements after shallow copying")
for i in range(0,len(li1)):
    print(li1[i],end=' ')
    
    


