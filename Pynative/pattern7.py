'''
    *
   * *
  * * *
 * * * *

'''

#total_rows = 4
#total_columns = 4

'''
R   Sp  St
1   3   1
2   2   2
3   1   3
4   0   4

spaces = total_rows - row
stars = row
'''

row = 1
total_rows = 4

while row <= total_rows:

    # print spaces
    space = 1
    while space <= total_rows - row:
        print(" ", end="")
        space += 1

    # print stars
    col = 1
    while col <= row:
        print("*", end=" ")
        col += 1

    print()
    row += 1
