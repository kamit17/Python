#Count how many words in a list have length 5.
def word_length(words):
    """Counts the number of words in a list which have length 5"""
    counter = 0
    for i in words:
        if len(i) ==5:
            counter += 1

    return counter

print(word_length(['Hello','Hi']))



