
"""
A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....

The first two terms are 0 and 1. All other terms are obtained by adding
the preceding two terms.This means to say the nth term is the sum of (n-1)th and
(n-2)th term.
"""

a = 0
b = 1
while b <50:
    c = a+b
    print(b)
    a = b
    b = c
    




"""def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)"""


"""
def fib(n):
    a = 0
    b = 1
    for i in range(1,n+1):
        c = a+b
        print(b)
        a = b
        b = c
fib(50)
"""
