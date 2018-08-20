# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 14:02:34 2018

@author: IEUser
"""
#program to prompt the user for  an original price and discount price and print out the price to nearest cent

def call(actual):
    print('First price is : ')
    FirstPrice = float(input())
    print('Discount is : ')
    Discount = float(input())
    


def actual(FirstPrice,discount):
    return(1-(discount/100))*FirstPrice