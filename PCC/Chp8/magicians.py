"""
8-9. Magicians: Make a list of magician’s names . Pass the list to a function called
show_magicians(), which prints the name of each magician in the list .
"""

def show_magicians(magicians_names):
    name = 0
    sizeoflist = len(magicians_names)
    while name < sizeoflist:
        print("\nThe magician's name is : ",magicians_names[name])
        name += 1
        """The same using a for loop is much clearer and easier to understand"""
    #for name in magicians_names:
       # print(name)

names = ['Medici','Merlin','PC Sarkar']
show_magicians(names)
