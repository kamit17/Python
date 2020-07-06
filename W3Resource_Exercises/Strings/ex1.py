# Write a Python program to calculate the length of a string
def string_length(str1):
    """Calculates the length of a string"""
    count = 0
    for letter in str1:
        count += 1
    return count

given_string= input("Enter the string: ")

print("The length of the given string : "+ given_string + " is ",string_length(given_string))
