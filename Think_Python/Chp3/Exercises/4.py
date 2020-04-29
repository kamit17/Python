# # Assume you have the assignment numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# # a. Write a loop that prints each of the numbers on a new line.
# # b. Write a loop that prints each number and its square on a new line.
# # c. Write a loop that adds all the numbers from the list into a variable called total.
# You should set the total variable to have the value 0 before you start adding them up, and print
# the value in total after the loop has completed.
# # d. Print the product of all the numbers in the list. (product means all multiplied together)

numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
total = 0
product=1
# a. Write a loop that prints each of the numbers on a new line.
for i in numbers:
    print( i)
# b. Write a loop that prints each number and its square on a new line.
for i in numbers:
    print(i, i **2)
    
for i in numbers:
    total += i
print('The sum of all the numbers in the list is : ',i,': ',total)

for i in numbers:
    product = product * i
print('The product of all the numbers in the list is: ',product)
    