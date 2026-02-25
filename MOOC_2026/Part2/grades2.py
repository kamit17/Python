'''
Write a program that takes test grades from the user and returns their average and the letter grade of the average.Use a while loop and make negative number the stop criteria. A >=90 B 80-89 C 70-79 D 60-69 F 59 or less
'''

total_sum = 0 # a container of stroing the sum of the values provided
num_count = 0 # a container for the number of values provided.

grade = int(input("Enter a grade (negative to quit): "))
#average = 0
while grade >=0:
    
    total_sum += grade
    num_count += 1
    grade = int(input("Enter a grade (negative to quit): "))
    
if num_count > 0:
    average = total_sum / num_count
    if average >=90:
        grade_letter = "A"
    elif average >=80:
        grade_letter = "B"
    elif average >=70:
        grade_letter = "C"
    elif average >=60:
        grade_letter = "D"
    else:
            grade_letter = "F"

            
    print("Average: ",average)
    print("Letter grade: ",grade_letter)
else:
    print("No grades were entered.")