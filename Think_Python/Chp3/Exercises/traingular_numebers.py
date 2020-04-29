
#Write a program that prints out the first n triangular numbers
"""
A triangular number is a number that can be shown using a pattern of dots in an equilateral
triangle.The nth triangular number is the number of dots in the triangular arrangement with n
dots on a side, and is equal to the sum of the n natural numbers from 1 to n

formular is n * (n+1)/2
"""

def triangular(n):
    x = 1
    while x <= n:
        formula = x * (x + 1) / 2
        print (x,'\t', formula)
        x += 1

triangular(5)
