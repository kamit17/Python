#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 21:32:08 2018

@author: Maverick
"""

#phoneAndEmail1.py - 

import re,pyperclip

# Create regex object for phone numbers
phoneRegex = re.compile(r'''(
((\d\d\d)|(\(\d\d\d\)))?
(\s|-)                  
-                  
\d\d\d\d                 
(((ext(\.)?\s)|x)      
(\d{2,5}))?)                                  
''',re.VERBOSE)

#Create a Regex for email address

emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+  
@    
a-zA-Z0-9_.+]+                     
''',re.VERBOSE)

# Extract the email/phone from this text
text = pyperclip.paste()

#TODO: Copy the extracted email/phone to the clipboard

extractedPhone = phoneRegex.findall(text)
extractedemail = emailRegex.findall(text)

print(extractedPhone)
print(extractedemail)