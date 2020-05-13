#Add a print function to Newton’s sqrt algorithm that prints out better each time it is
#calculated. Call your modified program with 25 as an argument and record the results.

"""
Newton's method for findind square roots
If you start with almost any approximation, you can computer a better approximation
with the following formula
better = (approximation + n/approximation)/2
"""

def newton(num):
    threshold = 0.001
    approximation = num/2
    while True:
        better = (approximation + num/approximation) /2
        if abs(approximation-better) < threshold:
            print(better)
            break
        approximation = better

newton(25)


