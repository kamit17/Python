"""
Exercise 3: Encapsulate this code in a function named count, and generalize it
so that it accepts the string and the letter as arguments.
"""

def count ( word, letter):
    count = 0
    for letter in word :
        if letter == 'a':
            count = count + 1

    return count

word = 'banana'
letter = 'a'
print(count(word,letter))
"""

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
"""
