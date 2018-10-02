#Python program to performa a global search over the whole input string  using re.findall() method.
#matchList = re.findall(pattern, input_str, flags=0)

import re
#Regex to match a few date strings
regex = r'[a-zA-Z]+ \d+'
matches = re.findall(regex,'October 02, September 23, Dec 1')
for match in matches:
	print('Full match: %s' %(match))
	
#To capture specific monthg of each date we can use the following pattern
regex1 = r'[a-zA-Z]+ \d+'
matches1 = re.findall(regex1,'October 02, September 23, Dec 1')
for match in matches1:
	print('Match Month: %s'%(match))
	
#if we need the exact position of each match
	
regex2 = r'[a-zA-Z]+ \d+'
matches2 = re.finditer(regex2,'October 02, September 23, Dec 1')
for match in matches2:
	print('Match is at index: %s,%s' %(match.start(),match.end()))