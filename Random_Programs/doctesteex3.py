'''
    >>> x + y
    42
    >>> type(message)
    <class 'str'>
    >>> len(message)
    13
'''
x = 21
y = 21
x + y
message = 'Hello Worlds!'

if __name__ == '__main__':
    import doctest
    doctest.testmod()
