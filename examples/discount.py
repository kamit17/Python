# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 14:02:34 2018

@author: IEUser
"""
#program to prompt the user for  an original price and discount price and print out the price to nearest cent


def newprice(x,y):
    new_price = (1-(x/100))*y
    return 'The new price  is {:.2f}'.format(new_price)
    
def main():
    #print(newprice(3,5))
    
   a = float(input('The discount is : '))
   b = float(input('The Original price is : '))
   print(newprice(a,b))
   
main()