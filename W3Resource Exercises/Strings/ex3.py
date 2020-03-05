"""
Write a Python program to get a string made of the first 2 and the last 2 chars
from a given a string. If the string length is less than 2, return instead of
the empty string. 
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
"""
def stringcon(str1):
    if len(str1) < 2:
        return ''

    return str1[0:2] + str1[-2:]


response = ''
while True:
    test_string = input('Enter the string to be tested: ')
    print(stringcon(test_string))
    print('Do you want another string to be tested? Yes to continue and No to exit ')
    response= input()
    if response == 'Yes':
        continue
    else:
        break
print('Thank you!')


