
"""
import random
joe = random.Random()
# Version 1
# Build a list of random numbers, then sum them
numbers = []
for _ in range(10000000):
    num = joe.randrange(1000) # Generate one random number
    numbers.append(num) # Save it in our list, see the next ˓→chapter
tot = sum(numbers)
print(tot)
"""
# Version 2
# Sum the random numbers as we generate them
import random
joe = random.Random()
tot = 0
for _ in range(10000000):
    num = joe.randrange(1000)
    tot += num
print(tot)