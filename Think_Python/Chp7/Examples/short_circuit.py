numbers = [11,8,33,17,16]
count =0
for number in numbers:
    count += number %2 == 1
    continue
print(count >0)