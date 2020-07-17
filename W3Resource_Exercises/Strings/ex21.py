#21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.


#str = "HeLlo"
def upper_case(str):
    num_upper = 0
    for i in str[0:4]:
        if i.upper() == i:
            num_upper += 1
            if num_upper >= 2:
                return( str.upper())
    return str
print(upper_case('HeLlo'))
#print(upper_case("HelLo" ))
