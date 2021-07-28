"""It is often useful to fetch data from a disk file and turn it into a list of lines. Suppose we have a file containing our friends and their email addresses, one per line in the file. But we’d like the lines sorted into alphabetical order. A good plan is to read everything into a list of lines, then sort the list, and then write the sorted list back to another file:"""

f = open("/Users/maverick/GitHub/Python/Think_Python/Chp13/Examples/friends.txt", 'r')

xs = f.readlines()
f.close
xs.sort()
g= open("/Users/maverick/GitHub/Python/Think_Python/Chp13/Examples/sortedfriends.txt" , "w")

for v in xs:
    g.write(v)
g.close()