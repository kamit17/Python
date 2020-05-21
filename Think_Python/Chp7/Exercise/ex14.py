#What will num_digits(0) return? Modify it to return 1 for this case. Why does a call to num_digits(-24) result in an infinite loop? (hint: -1//10 evaluates to -1) Modify num_digits so that it works correctly with any integer value. Add these tests:

def num_digits(n):
    return len(str(abs(n)))


assert num_digits(-100) == 3
assert num_digits(-99) == 2
assert num_digits(-11) == 2
assert num_digits(-10) == 2
assert num_digits(-9) == 1
assert num_digits(-1) == 1
assert num_digits(0) == 1
assert num_digits(1) == 1
assert num_digits(2) == 1
assert num_digits(9) == 1
assert num_digits(10) == 2
assert num_digits(11) == 2
assert num_digits(99) == 2
assert num_digits(100) == 3
assert num_digits(101) == 3
