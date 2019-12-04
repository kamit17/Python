"""
Return statement:
The return statement takes a value from inside a function and sends it back to the
line that called the function.

formatter_name.py: function that takes a first and last name, and returns a neatly formatted full
 name:
"""
def get_formatted_name(first_name,last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' '+ last_name
    return full_name.title()
    #print(full_name.title()) # not using a print since it returns none after displaiing output
    
musician = get_formatted_name('jimi','hendrix')
print(musician)
