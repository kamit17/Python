#6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. Go to the editor
#Sample String : 'abc'
#Expected Result : 'abcing'
#Sample String : 'string'
#Expected Result : 'stringly'


def string_end(given_string):
    length_given_string = len(given_string)
    if length_given_string > 2:
        if  given_string[-3:] == 'ing':  #if last 3 chars are ing
            given_string += 'ly'
        else:
            given_string += 'ing'

    return given_string

print(string_end('ab'))
print(string_end('string'))
print(string_end('happily'))



