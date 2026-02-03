'''Display quotient and remainder  problems with a function.
returning  a string and nor printing directly .
'''

def quotientString(x,y):
    quotient = x//y
    remainder = x%y
    quotientFormat = '{x} // {y} = {quotient} and {x} % {y} = {remainder}'
    solutions=quotientFormat.format(**locals())
    print(solutions)
  
    

def main():
    print(quotientString(2, 3))
    print(quotientString(1234567890123, 535790269358))
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    print(quotientString(a, b))

main() 