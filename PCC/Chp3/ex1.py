"""Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
rate for hours worked above 40 hours.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""

hours = float(input('Enter Hours: '))
rate =  float(input('Enter rate: '))
pay = 0.0
if hours < 40:
    pay = rate * hours
else:
    extra_hours = hours - 40
    pay = (1.5* rate*extra_hours ) + rate*40

print('Pay: ',pay)
