#17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
def extra_end(str):
    if len(str) < 2:
        return str
    return(str[-2:] * 4)

print(extra_end('Hello'))
