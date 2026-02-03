# The idea is to one by one extract all elements, place them at first position and recur for reamining list.

#Python function to print permutations of a fiven list
def permutation(lst):
    
    # if lst is empty, then there are no permutations
    if len(lst) == 0:
        return []
    
    #if there is only one elementin lst then, only one permutation is possible
    if len(lst) == 1:
        return [lst]
    
    #Find the permutations for lst if there are more than 1 characters
    
    l = [] #empty list that will store current permutation
    
    #iterate the input(lst) and calcualte the permutation
    for i in range(len(lst)):
        m = lst[i]
        
        #Extract lst[i] of m from the list. remLst is remaining list
        remLst = lst[:i] + lst[i+1:]
        
        #Generating all permutations where m is first element
        for p in permutation(remLst):
            l.append([m] + p)
    return l

data = list('123')
for p in permutation(data):
    print (p)