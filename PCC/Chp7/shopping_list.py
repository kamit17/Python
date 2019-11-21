"""
Grocery_list : Make a list called shoppint_list and fill it with the names of various
Groceries. Then make an empty list called shopping_cart. Loop
through the list of sshopping_list and print a message for each order, such
as This item has been added.  As each item is added , move it to the list
of shopping_cart. After all the items have been added, print a
message listing each item  that was added
"""
#make the shopping_list
shopping_list = ['rice','paper_towels','teabags','coffee','corflour']
shopping_cart = [] #The empty list

while shopping_list:
    #print(shopping_cart)
    current_item = shopping_list.pop()
    shopping_cart.append(current_item)

print('The following items are in the shopping cart: ')
for item in shopping_cart:
    print(item.title())

    

