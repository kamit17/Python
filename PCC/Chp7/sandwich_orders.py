"""
7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made.
"""
#Three steps to be taken
# Create the orders list and the finished list
sandwich_orders = ['Bagel toast','Baked Bean','Bologna','Pastrami','chicken']
finished_sandwiches = []

#loop through the list of sandwiches and print message for each order
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("\nI made your "+ current_sandwich.title()+ " sandwich.")
    finished_sandwiches.append(current_sandwich)

#After all the sandwiches have been made, print amessage listing each sandwich that was made.
print("\nI made the following sandwiche's for you!")
for sandwich in finished_sandwiches:
    print( sandwich.title() + ' Sandwich.')

