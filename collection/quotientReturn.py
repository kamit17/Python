'''Display quotient and remainder  problems with a function.
returning  a string and nor printing directly .
'''

def quotientString(x,y):
    quotient = x//y
    remainder = x%y
    return ('The quotient of  of {} and {} is {}.'.format(x, y, quotient))
    return ('The remainder of  of {} and {} is {}.'.format(x, y, remainder))
   
    #print('The quotient of  of {} and {} is {}.'.format(x, y, quotient))
    #print('The remainder  of {} and {} is {}.'.format(x,y,remainder))

def main():
    print(quotientString(2, 3))
    print(quotientString(1234567890123, 535790269358))
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    print(quotientString(a, b))

main() 