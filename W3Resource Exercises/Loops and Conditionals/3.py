"""
Write a Python program to guess a number between 1 to 9. Go to the editor
Note : User is prompted to enter a guess. If the user guesses wrong then the
prompt appears again until the guess is correct, on successful guess,
user will get a "Well guessed!" message, and the program will exit.
"""
import random 

guess = int(input("Enter an integer between 1 and 9: "))

number = random.randint(1,9)

while guess != number:
    guess = int(input('Wrong guess. Guess a number between 1 and 9: '))

print('Well guessed!')
