# Write a function that removes the first occurrence of a string from another string:

from test_suite import test

def remove(substring, string):
    sublen = len(substring)
    new_string = "" 

    for i in range(len(string)): 
        #find if slice of string and substring match.
        if string[i:i+sublen] == substring:
            #if true add slice and rest of string to new_string
            new_string += string[i+sublen:]
            break
        else:
             new_string += string[i] #add only the character = to loop 
                                     #variable
    return new_string

test(remove("an", "banana") == "bana")
test(remove("cyc", "bicycle") == "bile")
test(remove("iss", "Mississippi") == "Missippi")
test(remove("eggs", "bicycle") == "bicycle")