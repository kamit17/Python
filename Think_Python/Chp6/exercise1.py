def test_suite():
    assert turn_clockwise("N") == "E"
    assert turn_clockwise("E") == "S"
    assert turn_clockwise("S") == "W"
    assert turn_clockwise("W") == "N"
    assert turn_clockwise(42) == None
    assert turn_clockwise("rubbish") == None

    assert day_name(3) == "Wednesday"
    assert day_name(6) == "Saturday"
    assert day_name(42) == None

    assert day_num("Sunday") == 0
    assert day_num("Monday") == 1
    assert day_num("Tuesday") == 2
    assert day_num("Wednesday") == 3
    assert day_num("Thursday") == 4
    assert day_num("Friday") == 5
    assert day_num("Saturday") == 6
    assert day_num("Halloween") == None

    assert day_add("Monday", 4) == "Friday"
    assert day_add("Tuesday", 0) == "Tuesday"
    assert day_add("Tuesday", 14) == "Tuesday"
    assert day_add("Sunday", 100) == "Tuesday"
    assert day_add("Sunday", -1) == "Saturday"
    assert day_add("Sunday", -7) == "Sunday"
    assert day_add("Tuesday", -100) == "Sunday"

    assert days_in_month("February") == 28
    assert days_in_month("December") == 31
    assert days_in_month("Frubluary") == None

    assert to_secs(2, 30, 10) == 9010
    assert to_secs(2, 0, 0) == 7200
    assert to_secs(0, 2, 0) == 120
    assert to_secs(0, 0, 42) == 42
    assert to_secs(0, -10, 10) == -590
    assert to_secs(2.5, 0, 10.71) == 9010
    assert to_secs(2.433,0,0) == 8758

    assert hours_in(9010) == 2
    assert minutes_in(9010) == 30
    assert seconds_in(9010) == 10

    assert compare(5, 4) == 1
    assert compare(7, 7) == 0
    assert compare(2, 3) == -1
    assert compare(42, 1) == 1

    assert hypotenuse(3, 4) == 5.0
    assert hypotenuse(12, 5) == 13.0
    assert hypotenuse(24, 7) == 25.0
    assert hypotenuse(9, 12) == 15.0

    assert slope(5, 3, 4, 2) == 1.0
    assert slope(1, 2, 3, 2) == 0.0
    assert slope(1, 2, 3, 3) == 0.5
    assert slope(2, 4, 1, 2) == 2.0

    assert intercept(1, 6, 3, 12) == 3.0
    assert intercept(6, 1, 1, 6) == 7.0
    assert intercept(4, 6, 12, 8) == 5.0

    assert is_even(-2) 
    assert is_even(0)
    assert is_even(2)
    assert not is_even(-1)
    assert not is_even(1)

    assert is_odd(-1)
    assert is_odd(13)
    assert not is_odd(4)

    assert is_factor(3, 12)
    assert not is_factor(5, 12)
    assert is_factor(7, 14)
    assert not is_factor(7, 15)
    assert is_factor(15, 15)
    assert not is_factor(25, 12)

    assert is_multiple(12, 3)
    assert is_multiple(12, 4)
    assert not is_multiple(12, 5)
    assert is_multiple(12, 6)
    assert not is_multiple(12, 7)

    assert f2c(212) == 100
    assert f2c(32) == 0
    assert f2c(-40) == -40
    assert f2c(36) == 2
    assert f2c(37) == 3
    assert f2c(38) == 3
    assert f2c(39) == 4

    assert c2f(0) == 32
    assert c2f(100) == 212
    assert c2f(-40) == -40
    assert c2f(12) == 54
    assert c2f(18) == 64
    assert c2f(-48) == -54

    print("Ran the test suite")

def turn_clockwise(dir):
    """Takes a direction dir, in the form of a single letter N, E, S, or W. 
    Returns the direction 90 degrees clockwise from the input."""

    rotator = {"N": "E",
               "E": "S",
               "S": "W",
               "W": "N"
              }
    if dir in rotator:
        return rotator[dir]
    else:
        return None

def day_name(num):
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

def day_num(name):
    day_nums = {"Sunday": 0,
                "Monday": 1,
                "Tuesday": 2,
                "Wednesday": 3,
                "Thursday": 4,
                "Friday": 5,
                "Saturday": 6
    }
    if name in day_nums:
        return day_nums[name]
    else:
        return None

def day_add(weekday, add_num):
    start_num = day_num(weekday)
    end_num = (start_num + add_num) % 7
    end_name = day_name(end_num)
    return end_name

def days_in_month(x):
    month_lengths = {"January": 31,
                     "February": 28,
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
    if x in month_lengths:
        return month_lengths[x]

def to_secs(hours, minutes, seconds):
    return int(3600*hours + 60*minutes + seconds)

def hours_in(secs):
    return secs // 3600

def minutes_in(secs):
    return (secs % 3600) // 60

def seconds_in(x):
    return x % 60

def compare(a, b):
    if a > b:
        return 1
    if a == b:
        return 0
    if a < b:
        return -1

def hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5

def slope(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return dy / dx

def intercept(x1, y1, x2, y2):
    """Finds the y-intercept of a line given two points on it"""
    m = slope(x1, y1, x2, y2)
    # derived from the classic formula y = mx + b
    b = y1 - m * x1
    return b

def is_even(n):
    if type(n) == int:
        return n % 2 == 0

def is_odd(n):
    return not is_even(n)

def is_factor(f, n):
    return n % f == 0

def is_multiple(a, b):
    """Returns whether a is a multiple of b."""
    return is_factor(b, a)

def f2c(t):
    """Takes a temperature t in Fahrenheit and returns a Celsius 
    temperature rounded to the nearest degree."""
    return round( (t-32) / 1.8)

def c2f(t):
    """Takes a temperature t in Celsius and returns a Fahrenheit 
    temperature rounded to the nearest degree."""
    return round(1.8*t + 32)

test_suite()