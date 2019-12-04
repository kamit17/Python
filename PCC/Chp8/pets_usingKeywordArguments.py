"""
A keyword argument is a name-value pair that you pass to a function. You directly associate the
name and the value within the argument, so when you pass the argument to the function, there’s
no confusion .
"""
def describe_pet(animal_type,pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is "+ pet_name.title() + ".")

describe_pet(animal_type = 'hamster',pet_name = 'harry')
