# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 08:03:45 2018

@author: IEUser
"""
#! python3
import re,pyperclip
#TODO: Create a regex for URL
#https://google.com 
#http://google.com
#http://www.google.com
urlRegex = re.compile(r'''(
^(http:\/\/|https:\/\/)+   #http part (mandatory)
(www\.)?                    #optional www.
[a-zA-Z0-9.-]+               #domain name
(\.[a-zA-Z]{2,4})         #.com something
(:[0-9]{1,5})
)''',re.VERBOSE)

#TODO: Find matches in clipboard text
text = pyperclip.paste()

#matches = []

#extract the url to clipboard
urlextract = urlRegex.findall(text)
#Copy results to clipboard
print(urlextract)