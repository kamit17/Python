#Dictionaries Nesting example
# A list of dictionaries
#code to automatically generate each alien using range function

#Make an empty list for storing aliens.
aliens = []

#make 30 green aliens
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

#Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print('....')

#Show how many aliens have been created.
print('total number of aliens: ' + str(len(aliens)))