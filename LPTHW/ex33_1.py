"""
Convert this while-loop to a function that you can call,
and replace 6 in the test (i < 6) with a variable.
"""

def loop(max,step):
    i = 0
    numbers = []
    for i in range(0,max,step):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ",numbers)
        print(f"At the bottom i is {i}")
    return numbers

numbers = loop(10,2)

print('The numbers: ')

for num in numbers:
    print(num)
