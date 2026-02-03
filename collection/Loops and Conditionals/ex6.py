"""
6. Write a Python program to count the number of even and odd numbers from a
series of numbers. 
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4
"""
odd  = 0
even = 0
for i in range (0,9):
    if i %2  == 0:
        even +=1
    else:
        odd +=1
print("The count of even nmbers is ",even)
print("The count  of odd is ",odd)
