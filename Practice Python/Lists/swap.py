# Python program to swap first and last element of the list

def swap(newlist):
    size = len(newlist)

    #swapping
    temp = newlist[0]
    newlist[0] = newlist[size-1]
    newlist[size-1]= temp

    return newlist

newlist = [12,35,5,66,24]
print(swap(newlist))