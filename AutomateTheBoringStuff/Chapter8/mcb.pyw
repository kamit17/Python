#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Python program to keep track of multiple pieces of text.
#mcb.pyw - Saves and loads peieces of text to the clipboard

#Usage : py.exe mcb.pyw save <Keyword> - Saves clipboard to keyword
#		 py.exe mcb. pyw <keyowrd>- Loads keyword to cliboard
#		 pyr.exe mcd.pyw list - Loads all keywoards to cliboard.


import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#TODO : Save clipboard content.

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) ==2:

	#List keywords and load content
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()