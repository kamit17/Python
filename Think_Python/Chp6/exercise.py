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

test_suite()