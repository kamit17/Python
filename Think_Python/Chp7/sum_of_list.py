def mysum(xs):
    """Sum all the numbers in the list xs, and return the total."""
    runnin_total = 0
    for x in xs:
        running_total = running_total + x
    return running_total

#add tests like these to test your test suite....
test(mysum([1,2,3,4]),10)
test(mysum([1.25,2.5,1.75]),5.5)
test(mysum([1,-2,2.3]),2)
test(mysum([  ]),0)
test(mysum(range(11)),55)
