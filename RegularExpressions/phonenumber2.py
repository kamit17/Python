#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 21:02:46 2018

@author: Maverick
"""

import re
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  #call re.compile ()function to create a regex object.
mo = phoneNumRegex.search(message) #the search method searches the string for any matches to regex.If match is foud, returns a Match object.
print(mo.group()) #match objects have a group() mmethod that returns the actual mathced textfrom string .