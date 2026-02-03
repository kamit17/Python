#24. Write a Python program to check whether a string starts with specified characters

def specific_chars(str1,chars):
    if str1.startswith(chars):
        print("It starts with" , chars)
    else:
        print("it does not start with",chars)

string1 = input('Enter the string you want: ')
chars = input("enter the chars you want to test: ")

specific_chars(string1,chars)
