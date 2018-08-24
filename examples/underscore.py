# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 12:12:52 2018

@author: IEUser
"""

#program to take input from user and replace whitespace with _
s = str(input('Please enter a string : '))
sp = s.split()
print('_'.join(s))