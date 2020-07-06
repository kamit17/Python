"""
4. Write a Python program to construct the following pattern, using a nested
for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

"""

n = int(input("Enter the total number of rows you want: ")) #5 #total number of rows

for  i in range(n): #going hrough the number of rows
    for j in range(i): # going through the colums
        print("* ",end = '')
    print("")

for i in range(n,0,-1):
    for j in range(i):
        print('* ',end = "")
    print('')
