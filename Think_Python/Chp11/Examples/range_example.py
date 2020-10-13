from test_suite import test

def f(n):
    """Find the first positive integer between 101 and 
    less than n that is divisble by 21
    """
    for i in range(101,n):
        if ( i % 21 == 0):
            return i

test(f(110) == 105)
test(f(1000000000) == 105)