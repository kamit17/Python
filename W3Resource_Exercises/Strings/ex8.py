#Write a Python function that takes a list of words and returns the length of the longest one

def length_longest(words_list):
    word_len = words_list[0]
    for i in words_list:
        if len(i) > len(word_len):
            word_len = i
    return len(word_len)

a_list = ["Hello","Hi","Applebees","pineapple"]
print("The lenght of the longest word is: ",length_longest(a_list))


