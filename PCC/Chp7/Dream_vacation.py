"""
7-10. Dream Vacation: Write a program that polls users about their dream
vacation. Write a prompt similar to If you could visit one place in the world,
where would you go? Include a block of code that prints the results of the poll.
"""

responses = {}

name_prompt = "\nWhat is your name ? " 
place_prompt = "If you could visit one place in the world,where would you go?"
continue_prompt = "Do you want to continue? yes or no "

while True:
    #Asking the user where they want to go
    name = input(name_prompt)
    place = input(place_prompt)

    #Keep the respones
    responses[name] = place

    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

print("\n---Results---")
for name, place in responses.items():
    print(name.title() + " Would like to visit "+ place.title())