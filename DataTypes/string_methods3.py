# -*- coding: utf-8 -*-
#python code to demonstrate the working of center(),ljust() and rjust()

str = 'Assasin\'s Creed'
str1 = '12345'

#printing the string after centering it 
print('The string after centering is : ',end = '')
print( str.center(21,'-'))

#printing the string after ljust
print('The string after left justify is : ',end = '')
print( str.ljust(25,'='))


print('The string after right justify is : ',end = '')
print( str.rjust(25,'='))

# Checking if str has all alphabets 
if (str.isalpha()):
       print ("All characters are alphabets in str")
else : print ("All characters are not alphabets in str")

# Checking if str1 has all numbers
if (str1.isalnum()):
       print ("All characters are numbers in str1")
else : print ("All characters are not numbers in str1")
 
# Checking if str1 has all spaces
if (str1.isspace()):
       print ("All characters are spaces in str1")
else : print ("All characters are not spaces in str1")

#using join
print ( 'The string after joining is :' , end = '' )
print(str.join(str1))

#using join
print ( 'The string after split is :' , end = '' )
print(str.split('\n'))
