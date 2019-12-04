"""
Positional Arguments : Need to be in the same order as the parameters were written.

Function that displays information about pets.
"""
def describe_pet(animal_type,pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is "+ pet_name.title() + ".")

describe_pet("hamster","harry")
