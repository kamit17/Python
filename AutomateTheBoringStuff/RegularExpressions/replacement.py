#python program to find and replace string using re.sub() method
#replacedString = re.sub(pattern, replacement_pattern, input_str, count, flags=0)

import re
#Tryig to reverse the order of the day and month in a date string

regex = r'([a-zA-z]+) (\d+)'

print(re.sub(regex,r'\2 of \1','October 02, September 22, Dec 21'))