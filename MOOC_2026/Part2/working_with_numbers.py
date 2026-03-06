'''
Pre-task
Please write a program which asks the user for integer numbers. The program should keep asking for numbers until the user types in zero.

Part 1: Count
After reading in the numbers the program should print out how many numbers were typed in. The zero at the end should not be included in the count.

You will need a new variable here to keep track of the numbers typed in.

part 2
The program should also print out the sum of all the numbers typed in. The zero at the end should not be included in the calculation.

Part 3: Mean
The program should also print out the mean of the numbers. The zero at the end should not be included in the calculation. You may assume the user will always type in at least one valid non-zero number.

Part 4: Positives and negatives
The program should also print out statistics on how many of the numbers were positive and how many were negative. The zero at the end should not be included in the calculation.
'''

print("Please type in integer numbers.Type in 0 to finish. ")
total_num = 0  #Variable to keep track of numbers typed in
sum_total = 0  #variable to keep sum of the numbers excluding 0
positive_numbers = 0  #variable to keep count of positive numbers
negative_numbers = 0  #variable to keep count of negative numbers
while True:
    
    number = int(input("Number:"))
    
    if number ==0:
        break
    if number >0:
        positive_numbers += 1
    if number <0:
        negative_numbers +=1
    #part 2 condition
    total_num +=1
    #part3 condition
    sum_total = sum_total+number 
mean = sum_total/total_num
    
print("... the program asks for numbers")
print(f"Numbers typed in {total_num}")
print(f"sum of numbers {sum_total}")
print(f"Mean of the numbers is {mean}")
print(f"Positive numbers {positive_numbers}")
print(f"negative numbers {negative_numbers}")      



    
