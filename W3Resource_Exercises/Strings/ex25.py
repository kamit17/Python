#. Write a Python program to create a Caesar encryption.
#c = (x -n ) % 26 where x is the ASCII key of the  source message, n is the key, and 26 since there are 26 characters

def encrypted(string,shift):
    #empty string to hold the cipher
    cipher = ""
    #traversing the plain text
    for char in string:
        # if char is empty

        if char == " ":
            cpiher = cipher + char

        # Encrpyt uppercase characters in plain text
#note: The chr() function (pronounced “char”, short for “character”) takes an integer ordinal and returns a single-character string. The ord() function (short for “ordinal”) takes a single-character string, and returns the integer ordinal value.
        elif char.isupper():
            cipher = cipher + chr((ord(char)+shift-65)%26 + 65)

#Encrypt lower case characters in plain text
        else:
            cipher = cipher + chr((ord(char)+shift-97)%26 + 97)
    return cipher


text = input("enter the text: ")
s = int(input("Enter the shift key: "))
print("The original string is : ",text)
print('The encrypted msg is : ',encrypted(text,s))
