'''
* * * * *
* * * *
* * *
* *
*

'''

#row = 5
#col = 5
#as row increases, columns * decreses
#print * per columns


total_rows = int(input('Enter total_rows'))
row = 1
while row <=total_rows:
    columns = 1
    while columns <= total_rows - row +1:
        print('*', end = " ")
        columns += 1
    print()
    row +=1

