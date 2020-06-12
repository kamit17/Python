# Write a function that removes all occurrences of a string from another string:
from test_suite import test
def remove_all(substr, the_str):
    # replace method essentially removes variable substr
    new_string = the_str.replace(substr, "")
    return new_string

# get user input for example
# b_str = input("What string would you like to remove from?")
# a_str = input("What would you like to remove from that string?")
# print(remove_all(a_str, b_str))

test(remove_all("an", "banana") == "ba")
test(remove_all("cyc", "bicycle") == "bile")
test(remove_all("iss", "Mississippi") == "Mippi")
test(remove_all("eggs", "bicycle") == "bicycle")