from unit_tester import test
import string

def cleanword(s):
    """Remove punctuation from clean words"""
    s_without_punct=""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct +=letter
        split=s_without_punct.split()
    return s_without_punct   

def has_dashdash(s):
    """Check if string has double dash or not."""
    if s.find("--") == -1: #Don't have double dash
        return False
    else:
        return True 
    
def extract_words(s):
    """[summary]

    Args:
        s ([string]): [split words without punctuation and dash]
    """
    clean_s = ""
    for i in s:
        if i not in string.punctuation:
            clean_s += i
        else:
            i = " " # chancged punctuation to space
            clean_s += i
            
    n = clean_s.lower() # conver to lowercase
    return n.split()

def wordcount(word,seq):
    """ count spefic word in a sequence"""
    count = 0
    for i in seq:
        if i == word:
            count += 1
    return count
    
def wordset(seq):
    """find word set in a sequence"""
    w_set = []
    for i in sorted(seq):
        if i not in w_set:
            w_set.append(i)
    return w_set


def longestword(seq):
    """find the word which has the longest length"""
    length = 0
    for i in seq:
        if len(i) > length:
            length = len(i)
    return length        
    

#print(cleanword("?+='w-o-r-d!,@$()'"))
test(cleanword("what?") == "what")
test(cleanword("'now!'") == "now")
test(cleanword("?+='w-o-r-d!,@$()'") ==  "word")

test(has_dashdash("distance--but"))
test(not has_dashdash("several"))
test(has_dashdash("spoke--"))
test(has_dashdash("distance--but"))
test(not has_dashdash("-yo-yo-"))

test(extract_words("Now is the time!  'Now', is the time? Yes, now.") ==
      ['now','is','the','time','now','is','the','time','yes','now'])
test(extract_words("she tried to curtsey as she spoke--fancy") ==
      ['she','tried','to','curtsey','as','she','spoke','fancy'])


test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)



test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
      ["is", "now", "time"])
test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
      ["I", "a", "am", "is"])
test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
      ["a", "am", "are", "be", "but", "is", "or"])

test(longestword(["a", "apple", "pear", "grape"]) == 5)
test(longestword(["a", "am", "I", "be"]) == 2)
test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
test(longestword([ ]) == 0)