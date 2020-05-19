def next_collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def collatz_sequence(n):
    """ assembles a list based on next collatz function and then prints that list. """
    assert type(n) == int
    assert n > 0
    sequence = [n]
    while n != 1:
        n = next_collatz(n)
        sequence.append(n)
    return sequence

def collatz_steps(n):
    """For an integer n returns the number of steps before the Collatz function terminates at 1."""
    steps = 0
    while n !=1:
        n = next_collatz(n)
        steps +=1
    return steps

#for i in range(1,10):
#    print(collatz_sequence(i))

#for x in range (1,10):
#    print("{} takes {} steps to resolve.".format(x,collatz_steps(x)))

for x in range(1,100):
    if collatz_steps(x) > 100:
        print("{} takes {} steps to resolve.".format(x,collatz_steps(x)))
#        print(collatz_steps(x))
        break

high = 0
for x in range(1,10**6):
    this_result = collatz_steps(x)
    if this_result > high:
        high = this_result
        print(x,"takes",high,"steps")
