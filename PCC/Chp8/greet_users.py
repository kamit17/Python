""" greet users.py - program to print greeting to each user in the list."""

def greet_users(names):
    """print a simple greeting to each user in the list"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah','ty','margot']
greet_users(usernames)
