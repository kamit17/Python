# 1. Write a program to count how many odd numbers are in a list.

numbers =[10,20,30,15,11,17,25,22,31,999]

count = 0

for num in numbers:
    if  num % 2 == 0:
        continue
    else:
        count +=1
print(count)
    
#2Sum up all the even numbers in a list.

sum_even = 0
for num in numbers:
    if num %2 == 0:
        sum_even = sum_even+num
    else:
        continue
print(sum_even)

#Sum up all the negative numbers in a list.
sum_odd = 0
for num in numbers:
    if num %2 ==0:
        continue
    else:
        sum_odd += num
print(sum_odd)

#Count how many words in a list have length 5.
words = ['Hello','Hi', 'Welcome','Butyl','Vinyl','Orange']
word_count = 0
for word in words:
    if len(word) == 5:
        word_count += 1
    else:
        continue
print(word_count)

#5. Sum all the elements in a list up to but not including the first even number.
#(What if there is no even number?)
sum_elements = 0
for num in numbers:
    if num %2 == 0:
        break
    else:
        sum_elements = sum_elements+num
print(sum_elements)
    
#Count how many words occur in a list up to and including the first occurrence of the word “sam”
#(What if “sam” does not occur?)
word_count = 0
for word in words:
    if word != "sam":
        word_count += 1
    else:
        break
print('The word_count is :', word_count)