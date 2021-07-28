"""Another way of working with text files is to read the complete contents of the file into a string, and then to use our string-processing skills to work with the contents."""

# A simple example to count the number of words in a file

f = open("/Users/maverick/GitHub/Python/Think_Python/Chp13/Examples/friends.txt")
content = f.read()
f.close()

words = content.split()

print("There are {0} words in the file.".format(len(words)))