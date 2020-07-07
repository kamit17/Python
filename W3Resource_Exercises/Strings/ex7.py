# . Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# 
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

def find_string(given_string):
    pos_not = given_string.find('not')
    pos_poor = given_string.find('poor')
    
    if pos_not > pos_poor:
        given_string = given_string.replace(given_string[pos_not:(pos_poor+4)],'good')
        return given_string
    else:
        return given_string
    #return (pos_not,pos_poor)

print(find_string("The lyrics is not that poor!"))
