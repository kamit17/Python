#Write a version of Exercise for 
#Addition, add3f.py, that uses the 
#string format method to construct the
# same final string as before.

x = int(input("Enter an integer: "))
y = int(input("Enter another integer: "))
z = int(input('Enter another integer:'))
formatStr = '{0} + {1} + {2} = {3}'
sum = formatStr.format(x,y,z,x+y+z)
#print('The sum of ', x, ' ,', y, 'and',z, 'is ', sum, '.', sep='')
print('The sum of x,y,z is : ',sum)