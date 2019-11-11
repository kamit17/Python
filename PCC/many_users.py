'''
we store three pieces of information about each user: 
their first name, last name, and location. We’ll access 
this information by looping through the usernames and the 
dictionary of information associated with each username:
'''

users = {
    'aeinstesn':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },

}

for username,user_info in users.items():
    print('\nUsername: '+username)
    full_name = user_info['first']+" "+user_info['last']
    location = user_info['location']

    print('\tFull name: '+ full_name.title())
    print('\tLocation: '+ location.title())