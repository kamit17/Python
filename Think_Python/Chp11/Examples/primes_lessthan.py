def is_prime(n):
    if ( n ==1):
        return False
    elif (n ==2):
        return True
    else:
        for x in range(2,n):
            if(n %x ==0):
                return False
        return True

def primes_lessthan(n):
    """Returns a list of all prime numbers less than n."""
    result = []
    for i in range(2,n):
        if is_prime(i):
            result.append(i)
    return result

#print(is_prime(15))
print(primes_lessthan(15))