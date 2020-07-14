#12. Write a Python program to count the occurrences of each word in a given sentence

def word_count(sentence):
    """function to count the occurence of each word in a sentence"""
    words = sentence.split()
    d = {}
    for w in words:
        if w in d:
            d[w] +=1   # if word is aleardy in the dictionary increase the count by 1
        else:
            d[w]= 1    # if word is not in dictionary then add it to the dictionary count
    return d

print(word_count("This is a good day to  start something new."))

