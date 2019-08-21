#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 22:16:02 2018

@author: Maverick
"""

def maximum(x,y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y
    
print(maximum(2,3))