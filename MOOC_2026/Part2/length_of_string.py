'''
Please write a program which asks the user for a word and then prints out the number of characters, if there was more than one typed in.
'''    
word = input("Enter a word: ")

if len(word) > 1:
    print(f"Length of {word} is {(len(word))}")

print("Thank You.")