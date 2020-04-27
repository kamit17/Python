#  Write a fruitful function sum_to(n) that returns the sum of all
#  integer numbers up to and including n. So sum_to(10) would be
#  1+2+3. . . +10 which would return the value 55.

def sum_natural(n):
    """
        Function to calculate teh sum of n natural numbers
    """
 
    sum = 0
    for a in range(n+1):
        sum += a
    return sum
    
print(sum_natural(10))
    
