"""
7-10. Dream Vacation: Write a program that polls users about superpowers . Write a prompt similar to if you could have one superpower then what would it be? 
Include a block of code that prints the results of the poll.
"""

#a place holder dictionary  to store the responses
superpowers= {}
polling_active = True

#Write the prompts
#name_prompt = '\nWhat is your name? '
#question_prompt = '\nIf you could have one super power then what would it be ? '

while polling_active:
    #each pass through the while loop prompts for the user name and response
    name = input('\nWhat is your name? ')
    superpower= input('\nIf you could have one super power then what would it be ? ')

    #store the question in the dictionary
    superpowers[name] = superpower

    #find out if anyone else is going to take the quiz

    repeat = input('Would someone else take the quiz? (yes/no)')
    if repeat == 'no':
        polling_active = False

#Showing the results
for name,superpower in superpowers.items():
    print(name + ' Would like to have this superpower: ' + superpower)
