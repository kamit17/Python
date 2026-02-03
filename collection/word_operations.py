#load the words into a list using the below line

from os import closerange


wordlist = [line.strip() for line in open('wordlist.txt')]
file1=open('word_operations.txt','w')
print('-------Three lettered words-------',file=file1)
for word in wordlist:
    if len(word) ==3:
        print(word,file=file1)

print('Word starting with gn or kn',file=file1)
for word in wordlist:
    if word[:2]=='gn' or word[:2]=='kn':
        print(word,file=file1)

print('what percentage of words start with a vowel',file=file1)

count = 0
for word in wordlist:
    if word[0] in 'aeiou':
        count = count+1
print(100 * count/len(wordlist),file=file1)

#print all 7 letter words that start with th and end in ly
print("all 7 letter words that start with th and end in ly.",file=file1)
for word in wordlist:
    if len(word) ==7 and word[:2] =='th' and word[-2:] =='ly':
        print(word,file=file1)

#print the first words that start with q
print("The first 10 words that start with q are: ",file=file1)
i=0
while wordlist[i][0] !='q':
    i = i + 1
print(wordlist[i:i+10],file=file1)

# find the longest word that can be made using only the letters a.b.c.d and e

print("longest word that can be made using only the letters a.b.c.d and e",file=file1)
largest = 0
for word in wordlist:
    for c in word:
        if c not in 'abcde':
            break
        else:
            if len(word)>largest:
                largest=len(word)
                largest_word=word
print(largest_word,file=file1)

#find all words ending in ime
print('All words ending in ime',file=file1)
for word in wordlist:
    if word[-3:]=='ime':
        print(word,file=file1)

#words whose second, third, and fourth letters are ave
print("words whose second, third, and fourth letters are ave",file=file1)
for word in wordlist:
    if word[1:4]=='ave':
        print(word,file=file1)

#How many words contain at least one of the letters r, s, t, l, n, e
print("The total number of words that contain atleast one of r,s,t,l,n,e are: ",file=file1)
letter_count=0
for word in wordlist:
    for c in word:
        if c not in 'rstnlne':
            break
        else:
            letter_count +=1
print(letter_count,file=file1)


# the percentage of  words at least one of the letters r,s,t,l,n,e
print("The percentage of  words at least one of the letters r,s,t,l,n,e",file=file1)
print(100*letter_count/len(wordlist),file=file1)

#all words with no vowels
vowels =["a","e","i","o","u"]
answer_f =[]
for words in wordlist:
    if "a"  not in words and "e"  not in words and "i"  not in words and "o"  not in words and "u"  not in words:
        answer_f.append(words)       
print("all words with no vowles are \n",answer_f,file=file1)

#all words that contain a vowel
answer_e=[]
for words in wordlist:
    if "a" in words and "e" in words and "i" in words and "o" in words and "u" in words:
        answer_e.append(words)
#print("\n")
print("all words that contain vowelrs are \n",answer_e,file=file1)                     


#Where there are more ten-letter words or seven-letter words
count_ten=0
count_seven=0
for word in wordlist:
    if len(word) == 10:
        count_ten +=1
   
    if len(word) == 7:
        count_seven +=1
#print(count_seven)
#print(count_ten)
if count_ten > count_seven:
    print('There are more 10 letter words',file=file1)
else:
    print("there are more 7 letter words",file=file1)

#The longest word in the list 

longest = 0
for word in wordlist:
    if len(word) > longest:
        longest=len(word)
        longest_word=word
print(longest_word,file=file1)

#all palindromes
for word in wordlist:
    words = list(reversed(word))
    words = "".join(words)
    if word == words:
        
        print(words,word,file=file1)
        
#Same as above, but only print one word out of each pair.
for word in wordlist:
    words = list(reversed(word))
    words = "".join(words)
    if words == word:
        print(word,file= file1)
        

#All words that contain double letters next each other like aardvark or book, excluding words that end in lly

print("All words that contain double letters next each other like aardvark or book, excluding words that end in lly")      
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
answer_l = []
for words in wordlist:
    for letter in letters:
        if letter *2 in words and words[:-3] !="ily":
            answer_l.append(words)
print("\n")
print(answer_l,file=file1)


 #All words that contain a q that isn't followed by a u
 
       
file1.close()