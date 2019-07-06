#! python3

#Python code to find the url from an input string
#Using regular Expression

import re

def Find(string):
	url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
	string)
	return url
	

string = 'Url is:https://stackoverflow.com/questions/7048828/how-can-i-parse-multiple-unknown-date-formats-in-python'

print('Urls: ',Find(string))



 
