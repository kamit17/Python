# We use the find function . It returns the start position of the occurrence of a substring in the given string, then we increment this position by 1 and continue the search from that position till the end of ths tring

from test_suite import test
def count(substring,string):

    #initialize count and start to 0
    count = 0
    start = 0

    # search through the string till we reach the end of it
    while start< len(string):
        #check if a substring is present from start position till the end
        pos = string.find(substring,start)

        if pos != -1:
            # if a substring is present, move start to the next position from start of the substring
            start = pos + 1
            #increment the count
            count += 1
        else:
            break
    return count

test(count("is", "Mississippi") == 2)
test(count("an", "banana") == 2)
test(count("ana", "banana") == 2)
test(count("nana", "banana") == 1)
test(count("nanan", "banana") == 0)
test(count("aaa", "aaaaaa") == 4)