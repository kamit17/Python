#Write a Python program to count the number of characters (character frequency) in a string.

def char_count(input_string):
    """Funciton to calculate the character frequency in a string"""
    frequency = {}

    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

print(char_count('Data science'))
