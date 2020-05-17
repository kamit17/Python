#Count how many words occur in a list up to and including the first occurrence of the word “sam”. (Write your unit tests for this case too. What if “sam” does not occur?)

def sam_count(names):
    counter = 0
    for name in names:
        if name != 'sam':
            counter += 1
        else:
            break
    return counter

print(sam_count(['Harry','Bob','Dylan','Chris','sam','bill']))
