"""
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.
"""
sandwich_orders = ['Bagel toast','pastrami','Baked Bean','pastrami','Bologna','pastrami','chicken']
finished_sandwiches = []

print('The Deli has run out of  Pastrami.')

while 'pastrami'in sandwich_orders:
    sandwich_orders.remove('pastrami')
print('\nThe only reaming sandwiches are : ' )
print(sandwich_orders)

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("\nI made your "+ current_sandwich.title()+ " sandwich.")
    finished_sandwiches.append(current_sandwich)

#After all the sandwiches have been made, print amessage listing each sandwich that was made.
print("\nI made the following sandwiche's for you!")
for sandwich in finished_sandwiches:
    print( sandwich.title() + ' Sandwich.')
