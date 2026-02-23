'''
Write a program that takes integers from the user and returns the average. Use a while loop and make negative number the stop criteria.
'''

sum_values = 0 # a container of stroing the sum of the values provided
num_count = 0 # a container for the number of values provided.

input_value = int(input("Enter an integer. Enter a negative number to quit: "))

while input_value > 0: 
    print("condition1")    
    sum_values += input_value
    num_count +=1
    input_value = int(input("Enter an integer. Enter a negative number to quit: "))

if num_count > 0:
    print("Evaluating condition 2")
    average = sum_values/num_count
    print(f"Average of values is : {average}")
else:
    print("Exiting as negative number is entered")

