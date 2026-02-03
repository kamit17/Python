#Write a Python program to remove the nth index character from a nonempty string.
def remove_nth_index_char(str,n):
    return str[0:n] + str[n+1:]

print(remove_nth_index_char('sentence',2))
print(remove_nth_index_char('Banana',4))
print(remove_nth_index_char('Python',3))
