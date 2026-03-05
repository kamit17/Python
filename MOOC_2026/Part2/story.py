'''
Please write a program which keeps asking the user for words. If the user types in end, the program should print out the story the words formed, and finish.

Part 2

Change the program so that the loop ends also if the user types in the same word twice in a row.
'''

words = ""
#count = 0   #needed for part1
last_word = ""
while True:
    word = input("Please type in a word: ")
    '''needed for part1'''
    #f word == "end":
     #   break
    #count += 1   #needed for part1
    #words += word + " "
    '''part1 code above, part2 code below'''

    if word == "end" or last_word == word:
        break

    words += word + " "
    last_word = word

#print("You have typed in", count, "words.")
print("The story you created:")
print(words)