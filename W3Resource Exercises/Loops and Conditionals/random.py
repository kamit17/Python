from random import randint

number = randint(1, 9)
guess = int(input('guess a number between 1 and 9: '))

while guess != number:
    guess = int(input('you guessed wrong, guess again: '))

print('Well guesed!')
