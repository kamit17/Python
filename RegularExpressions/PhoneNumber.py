#PhoneNumber.py - A simple program to find phone number in a string without regular expressions.

def isPhoneNumber(text):
    if len(text) !=12:      #checks if string is exactly 12 characters   
        return False
    for i in range(0,3):
        if not text[i].isdecimal():   #checks if area code consists of only numeric characters
            return False
    if text[3] !='-':   #nneds to have a hyphen after the area code
        return False
    for i in range(4,7):
        if not text[i].isdecimal(): 
            return False
    if text[7] !='-':                
        return False
    for i in range(8,12):
        if not text[i].isdecimal():                
            return False
    return True                         
    
#print('415-555-4242 is a phone number:')
#print(isPhoneNumber('415-555-4242'))
#print('Moshi moshi is a phone number:')
#print(isPhoneNumber('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: '+ chunk)
print('Done')