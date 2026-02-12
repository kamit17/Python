#hourly_wage = float(input("Hourly wage: "))
#hours = int(input("Hours worked: "))
#day = input("Day of the week: ")
hourly_wage = 20.0
hours = 6
day = "Sunday"

daily_wages = hourly_wage * hours
print("condition:", day == "Sunday")
if day == "Sunday":
    print("wages before:", daily_wages)
    daily_wages *= 2
    print("wages after:", daily_wages)

print(f"Daily wages: {daily_wages} euros")