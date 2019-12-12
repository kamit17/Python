"""
8-10. Great Magicians: Start with a copy of your program from Exercise 8-9 .
Write a function called make_great() that modifies the list of magicians by adding
the phrase the Great to each magician’s name . Call show_magicians() to see that the
list has actually been modified .
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
        print(great_magician)
        great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)

magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)


""""
Just a rough outlay of the program
def show_magicians(magicians_names):
    for name in magicians_names:
       return (name)

def make_great(name):
    for i in name:
        print(i + ' the great')

names = ['Medici','Merlin','PC Sarkar']
great_magicians = []
show_magicians(names)
make_great(names)
"""
