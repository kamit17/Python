'''
A strong password is defined as one
that is at least eight characters long,
contains both uppercase and lowercase characters,
and has at least one digit.
You may need to test the string against multiple regex patterns to validate its strength.
'''
#Program to detect if password is strong or not

import re

#TODO: create Regex for password which mathes all the criteria above
pass_regex= re.compile(r'''
[a-zA-Z0-9@]{8,}
''',re.VERBOSE)

#TODO: Function to test above password regex
def pass_strength(pw):
	if re.match(pass_regex,pw):
		return True
	else:
		return False



#check if password is strong or not 
if __name__ == '__main__':
	pw = input('Enter your password: ')
	if pass_strength(pw):
		print('Strong password!')
	else:
		print('Weak Password')
	