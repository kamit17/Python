import re

#if separators should not be mixed use backreference:
date_reg_exp = re.compile('\d{4}(?P<sep>[-/])\d{2}(?P=sep)\d{2}')

# a string to test the regular expression above
test_str= """
     fsf2010/08/27sdfsdfsd
     dsf sfds f2010/08/26 fsdf 
     asdsds 2009-02-02 afdf
     """
# finds all the matches of the regular expression and
# returns a list containing them
matches_list=date_reg_exp.findall(test_str)

# iterates the matching list and prints all the matches
for match in matches_list:
  print (match)