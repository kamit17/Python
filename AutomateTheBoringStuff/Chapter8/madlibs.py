#!/usr/bin/python3

def mad_libs():
   
    filler = ['ADJECTIVE','NOUN','ADVERB','VERB']
    answer = []

    file = open('madlibs.txt','r')
    content = file.read().split()

    for word in content:
        if word.strip('.|!|?|,') in filler:
            answer.append(input('Enter a {0}: '.format(word)))
        else:
            answer.append(word)

    file = open('madlibs.txt','w')
    file.write(' '.join(answer))
    file.close()
mad_libs()