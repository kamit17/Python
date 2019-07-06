# -*- coding: utf-8 -*-
#python code to demonstrate working of string methods

str = '''Betty Botta bought a bit of butter.“But,” she said, “this butter's bitter!'''
str2 = 'butter'


#using startswith() to find if str starts with str2
if str.startswith(str2):
    print("str begins with str2")
else:
    print('str does not begin with str2')

#using endswith() to find if str ends with str2
if str.endswith(str2):
    print('str  ends with str2')
else:
    print('str does not end with str2')
    



# checking if all characters in str are upper cased
if str.isupper():
    print('All characters in str are upper case')
else:
    print('All characers in str are not upper case')

# checking if all characters in str1 are lower cased
if str2.islower() :
       print ("All characters in str1 are lower cased")
else : print ("All characters in str1 are not lower cased")

str =str.lower()
print('The lower case converted string is   : '+str)

str2 = str2.upper()
print('The upper case converted string is :  '+str2)

str3 = str.swapcase()
print('The swapped case  string is :  '+str)


str4 = str.title();
print ("The title case converted string is : " + str4)