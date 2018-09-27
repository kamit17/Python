# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 08:03:45 2018

@author: IEUser
"""
#! python3
import re,pyperclip
# Create a regex for URL

#urlRegex is advanced version which you can use to find anything after http or https
urlRegex = re.compile(r'''
http[s]?://   #http:// or https://
(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+
''',re.VERBOSE)

#Find matches in clipboard text
text = pyperclip.paste()

#extract the url to clipboard
urlextract = urlRegex.findall(text)
allUrls=[]
for url in urlextract:
    allUrls.append(url)

#Copy results to clipboard
results = '\n'.join(allUrls)
print(results)
#pyperclip.copy(results)
