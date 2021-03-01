import random

#create a black box object that generates a random number


rng = random.Random()

dice_throw = rng.randrange(1,100,7)  # Return an int, one of 1,2,3,4,5,6
delay_in_seconds = rng.random() * 5.0

print(dice_throw)


