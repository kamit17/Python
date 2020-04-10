#count digits that are only 0 or 5.
n = 2574301453
count = 0
while n > 0:
    digit = n % 10  # gives the remainder of n divided by 10
    if digit == 0 or digit == 5:
        count = count + 1
    n = n // 10  
print(count)