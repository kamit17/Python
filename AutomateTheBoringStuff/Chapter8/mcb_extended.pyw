#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Python program to keep track of multiple pieces of text.
#mcb_extended.pyw - Saves and loads peieces of text to the clipboard

#Usage : py.exe mcb.pyw save <Keyword> - Saves clipboard to keyword
#		 py.exe mcb. pyw <keyowrd>- Loads keyword to cliboard
#		 pyr.exe mcd.pyw list - Loads all keywoards to cliboard.


import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#TODO : Save clipboard content.

if len(sys.argv) == 3:
	if sys.argv[1].lower() == 'save':
		mcbShelf[sys.argv[2]] = pyperclip.paste()
	elif sys.argv[1].lower == 'delete':
		if sys.argv[2]:
			del mcbShelf[sys.argv[2]]
			pyperclip.copy('')


	
elif len(sys.argv) ==2:

	#List keywords and load content
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1].lower() =='delete':
		for key in  list(mcbShelf.keys()):

			del mcbShelf[key]
		pyperclip.copy('')

	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()
if __name__ == "__main__":
    pass