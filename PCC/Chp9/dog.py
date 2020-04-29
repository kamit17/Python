class Dog():  #1
    """ A simple attempt to model a dog""" #2

    def __init__(self,name,age):   #3
        """initialize name and age attributes."""
        self.name = name  #4
        self.age = age

    def sit(self):  #5
        """Simulate a dog sitting in response to a commnad."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in responses to a command."""
        print(self.name.title() + " rolled over!")
