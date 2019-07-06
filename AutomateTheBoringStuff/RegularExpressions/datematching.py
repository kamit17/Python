import re

#Regex matching dd/mm/yyyy
#[\d]{1,2} - match one or more digits
#[\d]{4} - match exactly 4 digits

str = "Today's date is 10/02/2018 , 11/22/2018 , 22-12-2014 02 October 2018, 22 Nov 2018"
regex= r'([\d]{1,2}/[\d]{1,2}/[\d]{4})'
all = re.findall(regex,str)
for s in all:
	print(s)
	
#Regex matching dd-mm-yyyy
#[\d]{1,2} - match one or two digits
regex1 = r'([\d]{1,2}-[\d]{1,2}-[\d]{2})'
all1 = re.findall(regex1,str)
for s in all1:
	print(s)

#Regex matching dd MMM yyyy
#[ADFJMNOS]\w* - Match big letter from ADFJMNOS followed by another letters

regex2 = r'([\d]{1,2} [ADFJMNOS]\w* [\d]{4})'
all2=re.findall(regex2,str)
for s in all2:
	print(s)
