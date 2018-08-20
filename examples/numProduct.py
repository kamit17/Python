# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 13:47:07 2018

@author: IEUser
"""


def product(nums):
    prod = 1
    for n in nums:
        print(prod)
        prod = prod*n
        
    return prod


print(product([5, 4, 6]))