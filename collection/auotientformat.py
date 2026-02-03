'''Display any number of quotient  problems with a function.
Handle keyboard input separately.
'''

def quotientFormat(x,y):
    quotient = x//y
    remainder = x%y
   
    print('The quotient of  of {} and {} is {}.'.format(x, y, quotient))
    print('The remainder  of {} and {} is {}.'.format(x,y,remainder))

def main():
    quotientFormat(2, 3)
    quotientFormat(1234567890123, 535790269358)
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    quotientFormat(a, b)

main() 
