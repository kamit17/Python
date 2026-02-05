hourly_wage = float(input("Enter your hourly wage: "))

hours_worked = int(input("Enter number of hours worked this week: "))
day_of_week = input("Enter the day of the week: ")
is_sunday = day_of_week.lower() == "sunday"
daily_wage= hourly_wage * hours_worked
#if day_of_week == "Sunday":
#    daily_wage=daily_wage*2
if is_sunday:
    daily_wage=daily_wage*2
print(f"Your total wage for the day is: {daily_wage} Euros")
