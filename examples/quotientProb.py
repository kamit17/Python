def quotientProblem(x,y):
    quotient = x//y
    remainder = x%y
    print('The Quotient  of {} and {} is {}.'.format(x,y,quotient))
    print('The remainder  of {} and {} is {}.'.format(x,y,remainder))
    



def main():
    quotientProblem(2, 3)
    quotientProblem(1234567890123, 535790269358)
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    quotientProblem(a, b)

main() 
