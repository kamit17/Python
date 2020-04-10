numbers = [11,13,33,17,19]
count =0
for number in numbers:
    count += number %2 == 1
print(count >0)