def print_multiples(n,high):
     for i in range(1,high+1):
         print(n * i,end = '  ')
     print()

def print_mult_table(high):
    for i in range(1,high+1):
         print_multiples(i,high)
#print_multiples(2)
print_mult_table(7)
