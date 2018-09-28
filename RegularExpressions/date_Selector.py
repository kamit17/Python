#! python3
# date_selector.py - Finds dates in different formats and pastes them in a single formats

import re
#TODO:Create a Regex for date
dateRegex = re.compile(r'''(
(\d|\d{2}|\d{4}|\w{1,4})  #match 1,2 or 4 digits or match word between 1 to 4
(-|\s|\.|\/)            #match either a dash or a space  or a period or a backslash
(\d{1,2}|\w{1,4})        #
(-|\s|\.|\/)
(\d{4}|\d{2})
)''',re.VERBOSE)

#Test the string
test_str = u"12-5-0000" #10.21.1955 10-21-1985 Aug-4-2018 6-5-1995 2004/2/21 5/25/2111 4999.2.21  5-June-2014"
#TODO:substitute the day with the format that you want

result= re.sub(r'(\d{4})(\d{2})(\d{2})', r'\2/\3/\1', test_str)
print(result)
#print(dateRegex.groups(0))
#matches = []                        #Store matches
##for groups in dateRegex.findall(test_str):
	##date = '-'.join([groups[1],groups[3],groups[5]])
	#matches.append(date)

#Copy  Results to the clipboard
#if len(matches) > 0:
	##print('\n'.join(matches))
#else:
	#print('Useless iterations.')
https://blog.softhints.com/python-regex-match-date/


