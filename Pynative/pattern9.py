'''
1
3 3
5 5 5
7 7 7 7
9 9 9 9 9

'''

'''
#total_rows = 5
#total_columns = 5
#Behavior --> Column increses as row increases
#each column is an odd number and  is 2 more than the numbe in the first row

'''
row =  1
while row <=5:
    col = 1
    while col <=row:
        print(2 * row -1, end = " ")
        col +=1
    print()
    row +=1
