"""
Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input

Enter Hours: forty
Error, please enter numeric input
"""
total_hours = 0.0
total_rate = 0.0
pay = 0.0

hours = input('Enter_hours: ')



try:
    total_hours = float(hours)

except:
    print('Please use numeric values')
rate = input('Enter rate: ')
try:
    total_rate = float(rate)
except:
    print('Please enter numeric value')

if hours < 40:
    pay = rate * hours
else:
    extra_hours = hours - 40
    pay = (1.5* rate*extra_hours ) + rate*40


print('Pay: ',pay)