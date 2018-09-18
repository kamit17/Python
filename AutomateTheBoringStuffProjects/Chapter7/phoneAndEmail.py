# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 15:08:23 2018

@author: IEUser
"""

#! python3
#phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard

import re, pyperclip
#TODO: Create a regex for phone numbers

phoneRegex = re.compile(r'''(
			\d{3}|\(\d{3}\))?                             #area code
			(\s|-|\.)?                                    
			(\d{3})                                       
			(\s|-|\.)                                    
			(\d{4})									        
			(\s*(ext|x|ext.)\s*(\d{2,5}))?                
			)''',re.VERBOSE)

#: create a regex for email addressses
emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+
        @
        [a-zA-Z0-9.-]+(\.a-zA-Z]{2,4}))''',
		re.VERBOSE)

#Find matches in clipboard text

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1],groups[3],groups[5]])
	if groups[8] !='':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])

#Copy  Results to the clipboard
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')

#TODO: Copy the extracted email/phone to the clipboard
