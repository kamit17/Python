from vocab_test import find_unknown_words
from test import test
import vocab_test

def load_words_from_file(filename):
    """ read words from  filename, return list of words"""
    f = open(filename,"r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds

bigger_vocab = load_words_from_file("vocabulary.txt")
# print("There are {0} words in the vocab, starting with\n {1} ".format(len(bigger_vocab),bigger_vocab[:6]))
#print(bigger_vocab)


def text_to_words(the_text):
    """return a list of words with all punctuation removed, and all in lowercase."""
    
    my_substitutions =  the_text.maketrans(  # If you find any of these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                          ")
    #Translate the text now
    cleaned_text = the_text.translate(my_substitutions)
    wds= cleaned_text.split()
    return wds

# test(text_to_words("My name is Earl!") == ["my", "name", "is", "earl"])
# test(text_to_words('"Well, I never!", said Alice.') ==["well", "i", "never", "said", "alice"])

def get_words_in_book(filename):
    """Read a book from filename, and return a list of its words. """
    f = open(filename,"r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds

book_words = get_words_in_book("AliceInWonderland.txt")
print('There are {0} words in the book, the first 100 are\n{1}'.format(len(book_words),book_words[:100]))

import time

t0 = time.clock()
missing_words = find_unknown_words(bigger_vocab, book_words)
t1 = time.clock()
print("There are {0} unknown words.".format(len(missing_words)))

#print(missing_words)
print("That took {0:.4f} seconds.".format(t1-t0))




#missing_words = find_unknown_words(bigger_vocab, book_words)