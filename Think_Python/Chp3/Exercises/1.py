"""
1 .Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to
Saturday. Write a program that asks a day number, and prints the day name
(a string).
"""

days = ["Sunday","Monday","Tuesday","Wednesday","Thursday",
        "Friday","Saturday"]
i = int(input('enter the value of i : '))
if i < len(str(days)):
    print(days[i])


