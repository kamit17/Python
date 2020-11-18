# Write a Python program to find the list of words that are longer than n from a given list of words.

# A string is given and you have to find all the words (substrings separated by a space) which are greater than given length .

#function find string greater than length n        
def string_k(n,str):
    
    #create the empty string
    string = []
    
    #split the string at space
    text = str.split(" ")
    
    #iterate the loop till every substring
    for i in text:
        
        #if length of current 
    
