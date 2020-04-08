#counts the number of decimal digits in a positive integer
n = 3029
count = 0
while n !=0:
    count = count + 1
    n = n //10
print(count)
