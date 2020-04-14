"""
You go on a wonderful holiday (perhaps to jail, if you don’t like happy exercises) leaving on
day number 3 (a Wednesday). You return home after 137 sleeps. Write a general version of the
program which asks for the starting day number, and the length of your stay, and it will tell
you the name of day of the week you will return on.
"""

days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
start_day = int(input("What day are you starting? select from 0 to 6: "))
length_of_stay = int(input("How many days are you staying?:  "))
return_date = (start_day + length_of_stay)%7   #total time % no of days in a week
print("The return date based on above information is : " , days[return_date])


                

"""
Same solution using function
def dayw(n):

    
    d = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    return d[n]
    

    
a = 3                 # starting day
b = 137               # lenth of stay away
c = dayw((a+b%7)%7)   # day of return
print(c)

"""