'''
Please write a program which asks the user for a year, and prints out the next leap year.

If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year:

'''

year = int(input("Please type in a year: "))

next_year = year + 1


while True:
    #check if next year is a leap year.
    if (next_year % 4 ==0 and next_year % 100 !=0) or (next_year %400 ==0):
        print(f"The next leap year after {year} is {next_year}")   
        break
    else:
        next_year = next_year + 1 
            
