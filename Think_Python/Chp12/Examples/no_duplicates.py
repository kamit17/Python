import random
xs = list(range(1,13)) #make list 1..12 ( there are no duplicates)
rng = random.Random() #make a random number generator
rng.shuffle(xs)       # shuffle the list
result = xs[:5]       #take the first five elements

print(result)