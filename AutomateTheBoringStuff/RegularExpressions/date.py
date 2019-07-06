import re
p = re.compile(ur'''(\d|\d{2}|\d{4})  # match 1 didget, or two didgets, or four didgets
    (\s|-|\.|\/) # match either a space or a dash or a period or a backslash
    (\d{2}|\d) # match either 2 digets or one
    (\s|-|\.\/) # match either a space or a dash or a period or a backslash
    (\d{4}|\d{2}) # match either 4 or 2 didgets.''', re.VERBOSE)
test_str = u"12/25/0000, 10.21.1955, 10-21-1985 6-5-1995 2004/2/21 5/25/2111 4999.2.21 "
 
re.search(p, test_str)
print(p.findall(test_str))
