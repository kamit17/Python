#This program says hellow and asks for myname

print('Hello World')
print('What is your name?') #Ask for their name
myName = input()
print('It is good to meet you, '+ myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?') #ask for their age
myAge = input()
print('you will be ' + str(int(myAge) + 1) + ' in a year')
