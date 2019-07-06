#Python code to demonstrate working of 
#strip(),lstrip(),rstrip
#min(),max()

str = '---Namaste London---'
str2 = 'Namaste'

#using strip to delete all ---
print('String after stripping is : ',end= '')
print(str.strip('-'))

#using lstrip to  delete all trailing '-'
print ( ' String after stripping all leading \'-\' is : ', end="")
print ( str.lstrip('-') )
#print('String after stripping all leading '-' is  :', end = '')
#print(str.lstrip('-'))

#using lrstrip to  delete all trailing '-'
print ( ' String after stripping all leading \'-\' is : ', end="")
print ( str.rstrip('-') )

#using min() to print the smallest character
print('The smallest character is : '+min(str2))

#using min() to print the largest character
print('The smallest character is : '+max(str2))