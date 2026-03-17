'''
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1

'''

'''

1       --->1
2 1     --->2
3 2 1   --->3
4 3 2 1 ---->4
5 4 3 2 1 -->5


row     column  numbers
1           1   1---------->row-col +1
2           2   2 1    > row - col + 1
3           3   3 2 1
4           4   4 3 2 1
5           5   5 4 3 2 1

column = row
number = row - col +1


'''



row = 1

while row <= 5:
    col = 1
    while col <= row:
        print(row - col + 1, end=" ")
        col += 1
    print()
    row += 1
