'''
Please make an extended version of the previous program, which prints out all the substrings which are at least three characters long, and which begin with the character specified by the user. You may assume the input string is at least three characters long.
Sample output

Please type in a word: mammoth
Please type in a character: m
mam
mmo
mot
Sample output

Please type in a word: banana
Please type in a character: n
nan

'''


word = input("Word: ")

character= input("What are you looking for: ")

while len(word) >3:
    if word[0] == character:
        print(word[:3])
    word = word[1:]