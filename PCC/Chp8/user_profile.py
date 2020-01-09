"""Python program to pass Arbitrary Keyword Arguments to a function"""

"""
Function build_profile takes in first and last name, but it accepts an arbitrary
number of keyword arguments as well.
"""
def build_profile(first,last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first #adding first name to dictionary
    profile['last_name'] = last   #adding last name to dictionary
    for key,value in user_info.items(): # looping through additional key value pairs in the dictionary user_info and add each pair to the profile dictionary.
        profile[key] = value
    return profile

user_profile = build_profile('albert','einstein',location = 'princeton',field = 'physics')

print(user_profile)
