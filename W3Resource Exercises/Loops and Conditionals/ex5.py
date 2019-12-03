"""
Write a Python program that accepts a word from the user and reverse it.

"""
word = input("Enter the word you want to be reversed: ")

count = len(word)
#print(count)
for i in range(count -1,-1,-1):
    print(word[i],end = "")
print("\n")
    
