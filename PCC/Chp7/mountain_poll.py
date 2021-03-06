#Filling a Dictionary with User input
#Polling program in which each pass through the loop prompts for the participant
#'s name and response.
#Store the data in  dictionary.

responses = {}

#Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    #Prompt for the person's name and response
    name = input('\nWhat is your name? ') #1
    response = input("Which mountain would you like to climb someday? ")

    #Store the responses in the  dictionary:
    responses[name] = response #2

    #Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no)")#3
    if repeat == 'no':
        polling_active = False

#Polling is complete. Show the results.
print("\n-- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
    
