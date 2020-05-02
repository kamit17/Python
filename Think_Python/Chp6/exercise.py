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
    
    #5th Test
    test(days_in_month("February")== 28)
    test(days_in_month("December") == 31)

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
test_suite()