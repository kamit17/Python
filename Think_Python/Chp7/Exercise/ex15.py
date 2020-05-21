#Write a function num_even_digits(n) that counts the number of even digits in n. These tests should pass:

#test(num_even_digits(123456) == 3)
#test(num_even_digits(2468) == 4)
#test(num_even_digits(1357) == 0)
#test(num_even_digits(0) == 1)

def num_even_digits(n):
    """Function to count number of even digits in nn"""
    n = abs(n)  #Strip off any potential negative symbol
    n = str(n)
    li
