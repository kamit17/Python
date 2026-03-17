'''
0 1 2 3 4 5
0 1 2 3 4
0 1 2 3
0 1 2
0 1
'''

#rows = 5
#columns = 5
#inverted pattern
'''
R       C
1       6
2       5
3       4
4       3
5       2
'''
row = 1

while row <=5:
    #print(row)
    col = 0
    while col <=5-row+1:
        print(col,end = " ")
        col +=1
    print()
    row +=1
