from C6_unit_tests import test


def test_suite():
    """Run the suite of test for code in the module
    """
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)
    test(turn_clockwise("S") == "W")
    test(turn_clockwise("E") == "S")
    
    #2nd Test
    test(day_name(2) == "Tuesday")
    test(day_name(6)== "Saturday")
    test(day_name(5) == "Wednesday")
    test(day_name(42)== None)
    
    
    #3rd Test
    test(day_num("Friday")== 5)
    test(day_num("Sunday")== 0)
    test(day_num(day_name(3))== 3)
    test(day_name(day_num("Thursday"))== "Thursday")
    test(day_num("Dullday") == 5)
    test(day_num("Halloween")== None)
    
    #4th Test
    test(day_add("Monday", 4) ==  "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")
    
    #6th Test
    test(days_in_month("February")== 28)
    test(days_in_month("December") == 31)
    test(days_in_month("Aprial") == None)
    
    #7th test
    test(to_secs(2, 30, 10)== 9010)
    test(to_secs(2, 0, 0)== 7200)
    test(to_secs(0, 2, 0)== 120)
    test(to_secs(0, 0, 42)== 42)
    test(to_secs(0, -10, 10)== -590)
    test(to_secs(2.5, 0, 10.71)== 9010)
    
#     9th test
    test(hours_in(9010)== 2)
    test(minutes_in(9010)== 30)
    test(seconds_in(9010)== 10)

# 11th test
    test(compare(5, 4)== 1)
    test(compare(7, 7)== 0)
    test(compare(2, 3)== -1)
    test(compare(42, 1)== 1)

#12th Test
    test(hypotenuse(3, 4) == 5.0)
    test(hypotenuse(12, 5) == 13.0)
    test(hypotenuse(24, 7) == 25.0)
    test(hypotenuse(9, 12) == 15.0)
    
    test(slope(5, 3, 4, 2)== 1.0)
    test(slope(1, 2, 3, 2)== 0.0)
    test(slope(1, 2, 3, 3)== 0.5)
    test(slope(2, 4, 1, 2)== 2.0)
 
#  13th test
    test(intercept(1, 6, 3, 12)== 3.0)
    test(intercept(6, 1, 1, 6)== 7.0)
    test(intercept(4, 6, 12, 8)== 5.0)
    
#14th test   
    test(is_even(-2))
#     test(is_even(-5))
# 15th test  
    test(is_odd(-1))
    test(not is_odd(4))
    
# 16th Test  
    test(is_factor(3, 12)== True)
    test(is_factor(5, 12)== False)
    test(is_factor(7, 14)== True)
    test(is_factor(7, 15)== False)
    test(is_factor(1, 15)== True)
    test(is_factor(15, 15)== True)
    test(is_factor(25, 15)== False)
    
# 17th test
    test(is_multiple(12, 3)== True)
    test(is_multiple(12, 4)== True)
    test(is_multiple(12, 5)== False)
    test(is_multiple(12, 6)== True)
    test(is_multiple(12, 7)== False)
    
# 18th test   
    test(f2c(212)== 100)     # boiling point of water
    test(f2c(32)== 0)        # freezing point of water
    test(f2c(-40)== -40)     # Wow, what an interesting case!
    test(f2c(36)== 2)
    test(f2c(37)== 3)
    test(f2c(38)== 3)
    test(f2c(39)== 4)
    
# 19th Test
    test(c2f(0)== 32)
    test(c2f(100)== 212)
    test(c2f(-40)== -40)
    test(c2f(12)== 54)
    test(c2f(18)== 64)
    test(c2f(-48)== -54)
    

# The four compass directions can be abbreviated by single-letter strings as “N”, “E”, “S”, and “W”.
# Write a function turn_clockwise that takes one of these four compass directions as its parameter,
# and returns the next compass direction in the clockwise direction. Here are some tests that should pass:


def turn_clockwise(direction):
    """Function that takes compass direction  and returns the next compass direction in the clockwise direction."""
    if direction in ['N','S','E','W']:
        if direction  == 'N':
            return 'E'
        elif direction == 'E':
            return 'S'
        elif direction == 'S':
            return 'W'
        elif direction == 'W':
            return 'N'
        return direction
    


#2Write a function day_name that converts an integer number 0 to 6 into the name of a day. Assumeday 0 is “Sunday”.

def day_name(num):
    """ Function to convert integer to name of day"""
    day_names = {0: "Sunday",
                 1: "Monday",
                 2: "Tuesday",
                 3: "Wednesday",
                 4: "Thursday",
                 5: "Friday",
                 6: "Saturday"
    }
    if num in day_names:
        return day_names[num]
    else:
        return None

# Write the inverse function day_num which is given a day name, and returns its number

def day_num(day):
    """Function to convert name of day to integer"""
    day_num = {"Sunday":0,
               "Monday":1,
               "Tuesday":2,
               "Wednesday":3,
               "Thursday":4,
               "Friday":5,
               "Saturday":6
               }
    if day in day_num:
        return day_num[day]
    else:
        return None
    
# 4 Write a function that helps answer questions like ‘“Today is Wednesday. I leave on holiday in
# 19days time. What day will that be?”’ So the function must take a day name and a delta argume
# -nt— the number of days to add — and should return the resulting day name

def day_add(weekday,num_days):
    """
        Function that takes start day and no. of days and returns the corresponding return date .
    """
    start_day = day_num(weekday)
    end_day =(start_day + num_days)%7
    end_name = day_name(end_day)
    return end_name

# 6 Write a function days_in_month which takes the name of a month, and returns the number of
#  days in the month. Ignore leap years

def days_in_month(name):
    """
        Function that takes the name of month and returns the number of days .
    """
    month_length = {
                    "January":31,
                    "February":28,
                    "March": 31,
                     "April": 30,
                     "May": 31,
                     "June": 30,
                     "July": 31,
                     "August": 31,
                     "September": 30,
                     "October": 31,
                     "November": 30,
                     "December": 31
                    }
    if name in month_length:
        return month_length[name]
    
# Write a function to_secs that converts hours, minutes and seconds to a total number of seconds.

def to_secs(hours,minutes,seconds):
    """Function to convert hours, minutues and seconds to total number of seconds"""
    convert = (3600 *hours + 60 *minutes+seconds)
    return int(convert)

# Write three functions that are the “inverses” of to_secs:    
# hours_in returns the whole integer number of hours represented by a total number ofseconds

def hours_in(seconds):
    return (seconds//3600)
    
#minutes_in returns the whole integer number of left over minutes in a total number ofseconds,
# once the hours have been taken out.

def minutes_in(seconds):
    return(seconds%3600)//60

# seconds_in returns the left over seconds represented by a total number of seconds

def seconds_in(seconds):
    return seconds % 60

# Write a compare function that returns 1 if a > b, 0 if a == b, and -1 if a < b

def compare(a,b):
    """ Function to compare """
    if a > b:
        return 1
    elif a ==b:
        return 0
    else:
        return -1
    

# Write a function called hypotenuse that returns the length of the hypotenuse of a right triangle given the lengths
# of the two legs as parameters:

def hypotenuse(base,height):
    """Function to return length of hypotenuse"""
    hypotenuse = (base **2 + height **2) ** 0.5
    return hypotenuse
    

#Write a function slope(x1, y1, x2, y2) that returns the slope of the line through the points (x1,y1) and (x2, y2)

def slope(x1, y1, x2, y2):
    """ Finds the slope of a line"""
    dy = y2-y1
    dx = x2-x1
    return (dy/dx)

# Then use a call to slope in a new function named intercept(x1, y1, x2, y2) that returns the y-intercept of the line
# through the points (x1, y1) and (x2, y2)

def intercept(x1, y1, x2, y2):
    """ Function that returns the y intercept of the line using the formula y = mx + b where b is the y intercept
         and m is the slope
    """
#     using the slope function to calculate m
    m = slope(x1, y1, x2, y2)
#     y = m * x + b
    b = y1 - m * x1
    
    return b
    
    
# Write a function called is_even(n) that takes an integer as an argument and returns True if theargument is an even
# number and False if it is odd.

def is_even(n):
    if type(n) == int:
        return n % 2 == 0
    
# Now write the function is_odd(n) that returns True when n is odd and False otherwise.Include unit tests for this
# function too.Finally, modify it so that it uses a call to is_even to determine if its argument is an odd integer,
# and ensure that its test still pass.

def is_odd(n):
#     not is_even(n)
    if n %2 !=0:
        return True
    else:
        return False

# 16
def is_factor(f, n):
    return n % f == 0

# 17
def is_multiple(x,y):
#     return (x % y ==0)
      return is_factor(y, x)
    
# 18 Write the function f2c(t) designed to return the integer value of the nearest degree Celsius forgiven tempurature
# in Fahrenheit. (hint: you may want to make use of the built-in function,round.)

def f2c(t):
    """Takes a temperature t in Fahrenheit and returns a Celsius 
    temperature rounded to the nearest degree."""
    return round( (t-32) / 1.8)

def c2f(t):
    """Takes a temperature t in Celsius and returns a Fahrenheit 
    temperature rounded to the nearest degree."""
    return round(1.8*t + 32)
    

test_suite()