 from test import test
 def find2(strng,ch,start):
     """Finds the location of the second or third occurence of a character in a string."""
     ix = start
     while ix < len(strng):
         if strng[ix] == ch:
             return ix
         ix += 1
        return -1
test(find2("banana","a",2)==3)
