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
