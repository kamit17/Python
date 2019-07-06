import re,pyperclip

#TODO: create Regex for password which mathes all the criteria above
pass_regex= re.compile(r'''
[A-Za-z0-9@]{8,}
''',re.VERBOSE)


def password_strength(text):
	if pass_regex.search(text) is None:
		return False
	else:
		return True
		
#get password from clipboard

pwd = str(pyperclip.paste())
print(pwd)
#check the strenght

if password_strength(pwd) is True:
	print("Strong Password")
else:
	print('Weak Password')