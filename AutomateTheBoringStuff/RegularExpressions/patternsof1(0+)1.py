#python program to find all the patterns of
#1(0+)1 in a given string using Python Regex

#1)Search a first sub-string in original string which follows'10+1'patterns
#using re.search(regex,string) method
#2)substr = re.search(regex,string) returns None if there is not match or else
#returns first matched substring which follows'10+1' pattern.
#substr.start() and substr.end() gives start and end index of matched regex
#3)Increse count by 1 whenever s match is found 

import re
#Function to find all the patterns of 1(0+)1 in a given string

def extract(input):
	#search regex '10+1' in original string
	#re.search() function returns first occurence
	#'10+1 - substring starts and ends with 1 and atleaset 1 or more 0 in between them
	count = 0
	substr = re.search('10+1',input)
	
	#search for regex in original string untill string completes
	while substr != None:
		#increase count if an match is found
		count = count+1
		
		#find next occurence 
		input = input[(substr.end()-1):]
		substr = re.search('10+1',input)
	print(count)
	

if __name__ == '__main__':
	input = '10101011'
	extract(input)