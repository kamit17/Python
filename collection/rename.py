#Automating Parsing and Renaming of Multiple files
import os
os.chdir('/Users/maverick/Downloads/DevOps')

#check if you are in correct locaoin
#print(os.getcwd())
#print out all of the files in this directory
for f in os.listdir():
	