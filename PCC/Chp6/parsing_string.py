"""finding a substring in a string
For example if we were
presented a series of lines formatted as follows:
From stephen.marquard@ uct.ac.za Sat Jan
5 09:14:16 2008
and we wanted to pull out only the second half of the address (i.e., uct.ac.za)
from each line, we can do this by using the find method and string slicing.
"""

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@') # find position of the @ sing
print('atpos',atpos)
sppos = data.find(' ',atpos) # find position of first space after @ sign
print('sppos',sppos)

host = data[atpos+1:sppos] # slice and extract the characters from one beyond the @ sing upto but not including the space character
print(host)
