#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 22:34:04 2018

@author: Maverick
"""

def simple_interest(p,r,t):
    SI = (p* r * t) /100
    return SI

def main():
    principle = float(input('Enter principle: '))
    time = int(input('Enter year: '))
    rate = float(input('Enter Rate: '))
    SI = simple_interest(principle,rate,time)
    print('The simple interest is : ',SI)
    
main()