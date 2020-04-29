from C6_unit_tests import test

# The four compass directions can be abbreviated by single-letter strings as “N”, “E”, “S”, and “W”.
# Write a function turn_clockwise that takes one of these four compass directions as its parameter,
# and returns the next compass direction in the clockwise direction. Here are some tests that should pass:
# test(turn_clockwise("N") == "E")
# test(turn_clockwise("W") == "N")

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
    
test(turn_clockwise("N") == "E")
test(turn_clockwise("W") == "N")
test(turn_clockwise(42) == None)
test(turn_clockwise("rubbish") == None)

# You should add all the unit tests you can think of.  I would also add
# these, even though they were not explicitly specified in the exercise:
test(turn_clockwise("S") == "W")
test(turn_clockwise("E") == "S")