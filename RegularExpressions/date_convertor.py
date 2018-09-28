#! python3
import re

regex = r'\b(0?[1-9]|[12]\d|3[01])([ \/\-])(0?[1-9]|1[012])\2(\d{4})'
test_str="Today's date is 10/5/2018"
subst = r'\3\2\1\2\4'
result = re.sub(regex,subst,test_str)
print(result)
#input("press Enter to continue")

