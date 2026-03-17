'''
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5

'''
#row = 5
#col = 5
#what is being printed --
#row 1 == 5 columns of row number each
#row 2 = 4 columns of row number each
#row 3 = 3 columns of row number
#row 4 = 2 columns of row number
#row 5 = 1 column of row number

row = 1

while row <= 5:
    col = 1
    while col <=6 - row:
        print(row, end = ' ')
        col +=1
    print()
    row +=1
