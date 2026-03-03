'''
Write a program that takes an integer number and outputs all the even numbers starting from 0 to the number
'''


number = int(input("enter a number: "))

counter = 0

while counter <=number:
    if counter  % 2 ==0:
        print(counter)
    counter +=1
