'''
Please write a program which asks the user to type in a limit. The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) until the sum is at least equal to the limit set by the user. 
'''

limit = int(input("Limit:"))
number = 1
sum = 0
while sum <=limit:
   #print(sum)
    sum += number
    number +=1
print(sum)

