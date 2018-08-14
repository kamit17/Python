def quotient(x,y):
    quotient = x//y
    remainder = x%y
    print('The Quotient  of {} and {} is {}.'.format(x,y,quotient))
    print('The remainder  of {} and {} is {}.'.format(x,y,remainder))
    



def main():
    quotient(2, 3)
    quotient(1234567890123, 535790269358)
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    quotient(a, b)

main() 
