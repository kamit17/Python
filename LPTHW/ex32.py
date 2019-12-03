the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

#for loop to go through a list
for number in the_count:
    print(f"This is count {number}")


#same as above
for fruit in fruits:
    print(f'A fruit of type: {fruit}')

#going through mixed list. using {} since we do not know what is in it
for i in change:
    print(f'I got {i}')

#we can also build lists,empty list
elements = []

#then use the range function to do 0 to 5 counts

for i in range(0,6):
    print(f'Adding {i} to the list.')
    #append to the list
    elements.append(i)

#print out the list
for i in elements:
    print(f'Element was: {i}')
