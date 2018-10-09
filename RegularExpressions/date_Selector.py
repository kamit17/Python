#! python3
# date_selector.py - Finds dates in different formats and pastes them in a single formats

import re
dateRegex = re.compile(r'''(
(\d{1,2}|d{4}|[a-zA-Z]) #matches 1,2 or 4 digits or characters between a-z
(\s|-|\.|\/)  #matches either space,dash ,period or backslash
(\d{1,2}|[a-zA-Z])  #matches 2or 1 digits or a-z characters
(\s|-|\.|\/) 
(\d{4}|\d{2}) #match either 4 or 2 digits
)''',re.VERBOSE)

test_str = "Jan/12/2018 12/22/2010 10.21.2016, 17-01-1986 01/17/1986 Jan 17 1986"

re.search(dateRegex, test_str)
print(dateRegex.findall(test_str))
#https://blog.softhints.com/python-regex-match-date/


