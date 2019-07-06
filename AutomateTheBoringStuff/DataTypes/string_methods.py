# -*- coding: utf-8 -*-
# python code to demonstrate working of
# find() and rfind()

str = '''Betty Botta bought a bit of butter.“But,” she said, “this butter's bitter!'''
str2 = 'butter'

# using find() to find first occurrence of str2
print('The first occurrence of str2 is at : ', end='')
print(str.find(str2, 13))


# using rfind to find last occurrence of str2
print('The last occurrence of str2 is at : ', end='')
print(str.rfind(str2, 13))


#printing lenght of string using len()
print(" The length of string 1 is : ", len(str))

#using count to check the number of occurences of butter in str
print("Number of occurences of ""butter"" is : ",end='')
print(str.count("butter",0,74))




