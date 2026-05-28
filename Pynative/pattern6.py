'''
5 5 5 5 5
5 5 5 5
5 5 5
5 5
5

'''

#rows -->5
#columns ->5

#row increases --> columns decreses
#print 5
'''
Row         Count     Row + col
1            5          6
2            4          6
3            3          6
4            2          6
5            1          6
'''

#column <= total_row - rownumber + 1


total_rows = int(input("Enter the number or rows: "))

row = 0
while row <= total_rows:
    col = 0
    while col < total_rows - row + 1:
        print(total_rows,end = " ")
        col += 1
    print()
    row += 1
