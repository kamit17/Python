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
			(\s|-|\.)?                                    #Seperator
			(\d{3})                                       #first 3 digits
			(\s|-|\.)                                     #seperator
			(\d{4})									        #last 4 digits
			(\s*(ext|x|ext.)\s*(\d{2,5}))?                #extension
			)''',re.VERBOSE)

#TODO: create a regex for email addressses
emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+
        @
        [a-zA-Z0-9.])
                        )

#TOTO: Get the text off the clipboard

#TODO: Extract the email/phone from this text

#TODO: Copy the extracted email/phone to the clipboard