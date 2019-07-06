import re

password = input('Enter string to test: )

if re.match(r'[A-za-z0-9@#$%^&+=]{8,}',password):
	print("password is valid")
else:
	print("Password is invalid")