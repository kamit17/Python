"""
8-11. Unchanged Magicians: Start with your work from Exercise 8-10 . Call the function
make_great() with a copy of the list of magicians’ names . Because the original list
will be unchanged, return the new list and store it in a separate list . Call
show_magicians() with each list to show that you have one list of the original names
and one list with the Great added to each magician’s name .
"""
def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Add 'the Great!' to each magician's name."""
    # Build a new list to hold the great musicians.
    great_magicians = []

    # Make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)
    return magicians

magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)

print("\n")
print("Great magicains")
#great_magicians = make_great(magicians[:])
show_magicians(make_great(magicians[:]))

print("\n")
print("original magicians:")
show_magicians(magicians)
