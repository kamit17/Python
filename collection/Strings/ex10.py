#Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
def exchange(str):
    return str[-1:]+ str[1:-1] + str[:1]

print(exchange('sentence'))
print(exchange('12345'))
