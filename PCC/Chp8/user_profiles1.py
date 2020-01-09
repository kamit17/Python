"""
8-13.
User Profile: Start with a copy of user_profile.py from page 153 . Build
a profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you .
"""
def build_profile(first,last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first #adding first name to dictionary
    profile['last_name'] = last   #adding last name to dictionary
    for key,value in user_info.items(): # looping through additional key value pairs in the dictionary user_info and add each pair to the profile dictionary.
        profile[key] = value
    return profile

user_profile = build_profile('jack','shirley',location = 'Little Rock',
                             field = 'computer science',career = 'Data science',phone = 'Iphone6s')

print(user_profile)
