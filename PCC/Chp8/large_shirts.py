"""
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python . Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message .
"""
def make_shirt(size = "Large", message = "I Love python"):
    print("The size of the shirt is " + size +" and the message on the shirt is "+ message.title())

make_shirt()
make_shirt(size = "medium")        
