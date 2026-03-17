'''
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''

'''
R   C   Number Printed

1   1   5  5 -1 + 1
2   2   4  5 - 2 + 1
3   3   3  5 - 3 + 1
4   4   2  5 - 4 + 1
5   5   1  5 - 5 +1

'''

#columns = row
#number = 5 - row + 1
'''
row = 1
while row <=5:
    col = 0
    while col <= 5-row +1 :
        print(5-row+1, end = " ")
        col +=1
    print()
    row +=1

'''

row = 1

while row <= 5:
    col = 1

    while col <= 5 - row + 1:
        print(5 - row + 1, end=" ")
        col += 1

    print()
    row += 1
