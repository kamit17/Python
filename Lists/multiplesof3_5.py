#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 21:04:33 2018

@author: Maverick
"""
total=0
print(list(range(1,100)))
for i in list(range(1,100)):
    if (i%3 == 0 or i % 5 == 0):
        total +=i 
#print(list(range(1,100)))
#print (total)
print('The total of the multiples of  3 and 5 is :  '+str(total))
        