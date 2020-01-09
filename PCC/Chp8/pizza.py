#Passing an aribitrary Number of Arguments
def make_pizza(*toppings):
 # the * in the parameter tells python to make an empty tuple andpack
 #whatever value it receives into this tuple.
    #"""Print the list of toppings you have requested"""
    #print(toppings)
     """Summarize the pizza we are about to make"""
     print("\nMaking a pizza with the following toppings:")
     for topping in toppings:
         print("- " + topping)


make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
    

 
    
    
