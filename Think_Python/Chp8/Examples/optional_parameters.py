from test import test
def find(strng,ch,start=0):
    ix = start
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix +=1
    return -1
test(find("banana","a",7) ==7)
