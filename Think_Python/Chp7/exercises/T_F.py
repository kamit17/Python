#Write a program which prints True when n is a prime number and False otherwise.

def is_prime(n):
    x = n - 1
    
    #if n is less than 2, its 0/1
    #which is not conventionally a prime number
    if n < 2:
        return False
        
    #if n is 2 then its a prime number!
    if n == 2:
        return True
        
    while x > 1:
        if n % x == 0:
            return False
        else:
            x -= 1       
    return True  

print(is_prime(5))
print(is_prime(8))
                

