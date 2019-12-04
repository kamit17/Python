"""
8-5. Cities: Write a function called describe_city() that accepts the name
of a city and its country . The function should print a simple sentence,
such as Reykjavik is in Iceland . Give the parameter for the country a
default value . Call your function for three different cities, at least one
of which is not in the default country .
"""
def describe_city(name,country = "iceland"):
    print(name.title() + " is the capital of " + country.title())

describe_city("reykjavik")
describe_city("new delhi","india")
describe_city("bucharest","romania")
    
