#Write a Python program to remove duplicates from  a list

def duplicate_test(sample):
    
    duplicate = set()
    unique = []
    
    for i in sample:
        if i not in duplicate:
            unique.append(i)
            duplicate.add(i)
            
    #return unique
    return duplicate


a = [10,20,30,20,10,50,60,40,80,50,40]

print('The Duplicates are : ' ,duplicate_test(a))
#print('The non duplicates are :',duplicate_test(a))
