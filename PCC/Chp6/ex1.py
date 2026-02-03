"""
Exercise 1: Write a while loop that starts at the last character in the string
and works its way backwards to the first character in the string, printing each
letter on a separate line, except backwards.

"""
"""
index = 0
word = input("Enter the word: ")

while index < len(word):
    index = index -1
    letter = word[index]
    print(letter)
    
"""

fruit = 'banana'
index = len(fruit) -1   # setting the index to the last character
while index >= 0:
  print (fruit[index])
  index -= 1
  
  """

while index < len(fruit):
  index = index -1
  letter = fruit[index]
  print(letter)
"""
