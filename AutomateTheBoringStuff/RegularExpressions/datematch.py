#Python program to to test whether a regular expression matches a specific string in Python, using re.search()
#matchObject = re.search(pattern, input_str, flags=0)
import re

regex = r'([a-zA-Z]+) (\d+)'

if re.search(regex,'October 02'):

	#using the Match Object's start() and end() methods 
	#to retreive where the pattern matches in the input string, and the
	# group() method to get all the matches and captured groups
	match = re.search(regex,'October 02')
	
	#This will print[0,10), since it matches at the beginning  and end of the string
	print("Match at index %s, %s" % (match.start(), match.end()))
	
	#The group containts the matched values. 
	#match.group(0) always returns the fully matches string
	#match.group(1),match.group(2),... will return the captured
	#groups in order from left to right in the input string
	#match.group() is equilvalent to match.group(0)
	
	#This will print October 02
	print("Full match: %s" % (match.group(0)))
	
	#This will print "October"
	print("Month: %s" % (match.group(1)))
	
	#This will print "02"
	print("Day: %s" % (match.group(2)))
	
else:
	#if re.search() does not match, then None is returned 
	print('The regex pattern does not match. :( ')