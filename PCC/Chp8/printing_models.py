"""
Consider a company that creates 3D printed models of designs that users submit.
Designs that need to be printed are stored in a list, and after being printed
they’re moved to a separate list.
The following code does this without using functions:
"""

#Start with some designs that need to be printed
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

#Simulate printing each design, until none are left
#Move each design to completed_models after printing.

while unprinted_designs:
    current_design = unprinted_designs.pop()

    #simulate creating a 3D print fromo the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

#Display all completed models.
print("\nTHe following models have been printed.")
for completed_model in completed_models:
    print(completed_model)
