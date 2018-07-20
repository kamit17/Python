#python code to demonstrate working of startwith() and endswith()

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
