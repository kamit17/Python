'''
*
* *
* * *
* * * *

'''

#how many rows == 4
#how many things print in each row
#row 1 -- 1 *
#row 2 -- 2 *
...
#row 4 -- 4 *

#columns = row numbers
#what should be printed -- *  * *
'''
rows = 4
columns = row
print = *

'''

rows = 1

while rows <=4:
    col = 1
    while col <= rows:
        print('*', end = " ")
        col += 1
    print()
    rows += 1
