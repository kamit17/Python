#implementation
#Refer this link : https://inventwithpython.com/chapter14.html
#We can do this by represneting each letter as a number called ordinal  and then adding or subtracting from this number to form a new ordinal.
#The chr() function (pronounced “char”, short for “character”) takes an integer ordinal and returns a single-character string. The ord() function (short for “ordinal”) takes a single-character string, and returns the integer ordinal value.

#The key cannot be more than 26
MAX_KEY_SIZE = 26

#deciding to decrypt or encrypt
def getMode():
    while True:
        print('Do you wan to encrypt or decrypt a message? ')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

#Get the message from the player
def getMessage():
    print("Enter your message: ")
    return input()

#Get the key from the player
def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' %(MAX_KEY_SIZE))  #%26 so that we can handle loop around .https://teachen.info/cspp/unit4/lab04-02.html
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode,message,key):
    if mode[0] =='d':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -=26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num >ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        else:
            translated += symbol
    return translated

mode = getMode()
message = getMessage()
key = getKey()

print('Your translated text is: ')
print(getTranslatedMessage(mode,message,key))


