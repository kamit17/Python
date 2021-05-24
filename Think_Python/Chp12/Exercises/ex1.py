import calendar
cal = calendar.TextCalendar() #create an instance
calendar.setfirstweekday(calendar.THURSDAY)
print("Calendar with week starting on Thursday:")
cal.pryear(2021)
print("Calendar Returning Birthday Month")

print(calendar.month(2021,1))

#d = calendar.LocaleTextCalendar(6,"SPANISH")
#d.pryear(2012)

print(calendar.isleap(2016))