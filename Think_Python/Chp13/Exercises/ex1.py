#Write a program that reads a file and writes out a new file with the lines in reversed order (i.e. the first line in the old file becomes the last one in the new file.)
"""
f1 = open("reverse.txt","w")

#open the input file and  get the contents into a variable data

myfile=open("friends.txt","r")
data = myfile.read()

data_1 = data[::-1]

f1.write(data_1)

f1.close()

"""

#reversing the order of lines

f2 = open("reverse_order.txt","w")

myfile=open("friends.txt","r")
data = myfile.readlines()

#reverse the array using the following
data_2= data[::-1]

f2.writelines(data_2)
f2.close()