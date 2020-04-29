def find_first_2_letter_word(words):
    """ Function which looks through a list of words and returns the
        first 2 letter word.
    """
    for word in words:
        if len(word) == 2:
            return word
        return ""

words = ["This","is","a","dead","parrot"]
print("The first 2 letter word  ",find_first_2_letter_word(words))

find_first_2_letter_word(["I","like","Cheese"])