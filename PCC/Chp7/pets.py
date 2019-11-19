#Removing all instance of Specific values from a List
pets = ['dog','cat','dog','cat','goldfish','turtle','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print('pets')
