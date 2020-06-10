#Encapsulate
def count_letters(string,ltr):
    """Count the number of times a character appears in a string"""
    count = 0
    for char in string:
        if char == ltr:
            count +=1
    return count

print(count_letters("banana","a"))
