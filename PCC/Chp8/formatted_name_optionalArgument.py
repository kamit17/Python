"""making an argument optional"""
"""
To make the middle name optional, we can give the middle_name argument an empty default value
and ignore the argument unless the user provides a value. To make get_formatted_name() work
without a middle name, we set the default value of middle_name to an empty string and move it
to the end of the list of parameters:

"""
def get_formatted_name(first_name,last_name,middle_name = ''):
    """Return a full name, neatly formatted."""
    if middle_name: #if the con
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " "+ last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('lee','john','blackmore')
print(musician)
