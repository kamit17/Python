#This is a guess the number game .
import random

print('Hello. what is your name ?')
name = input()

print('Hello, ' + name + ', Iam thinking of a number between 1 and 20.')

secretNumber = random.randint(1,20) 

#Ask the player to guesss 6 times
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())
    
    if guess < secretNumber:
        print('your guess is too low.')
    elif guess > secretNumber:
        print('your guess is too high')
    else:
         break  # This condition is the correct guess!

if guess == secretNumber:
    print('Good job' + name + 'You guessed my number in '+ str(guessesTaken)+'guesses')
else:
    print('Nope. The number I was thinking of was '+str(secretNumber))
 