'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

'''

#rows = 5
#columns = 5
#what is changing -- each row the number of columns increases, the column number increases by 1 in each column
#what is being printed -- row numbers

row  = 1


while row <=5:
    col = 1
    while col <=row:
        print(row,end = ' ')
        col +=1
    print()
    row += 1
