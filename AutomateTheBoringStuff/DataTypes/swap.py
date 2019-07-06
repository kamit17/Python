#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 20:34:24 2018

@author: Maverick
"""



b = ["banana","apple","Microsoft"]
print(b)
#temp = b[0]
#b[0] = b[2]
#b[2] = temp
b[0],b[2] = b[2],b[0]
print(b)
