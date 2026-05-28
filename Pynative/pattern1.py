#Write a Python code to print the following number pattern using a loop.
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

#how many rows  =5
#what changes every rwo --> each row prints one more number than the previous row
#row number  = how many numbers to print
#outerloop --- controls rows
#inner loops --> numbers in that row

row = 1


while row <=5:
    col = 1
    while col <=row:
        print(col,end = " ")
        col +=1
    print()
    row +=1

