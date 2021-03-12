import random

def make_random_ints_no_dups(num, lower_bound,upper_bound):
    """
    generate a list containing num random ints between lower_bound and upper_bound.The result cannot contain duplicates.

    Args:
        num (int): initial number
        lower_bound (int): lower bound
        upper_bound (int): open bound .
    """
    
    result = []
    rng = random.Random()
    for i in range(num):
        while True:
            candidate = rng.randrange(lower_bound,upper_bound)
            if candidate not in result:
                break
        result.append(candidate)
    return result

#xs = make_random_ints_no_dups(5,1,1000000)
xs = make_random_ints_no_dups(10,1,6)
print(xs)