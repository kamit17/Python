def get_cipherletter(new_key,letter):
    """Function to return the new letter given a new key"""
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter in alpha:
        return alpha[new_key]
    else:
        return letter

def encrypt(key,message):  #take in key and message as argument
    """Function for encryption"""
    #convert the message to uppercase
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # hold the alphabet as a long string
    #initialize empty string to store stresult
    result = ""

#Ceaser cipher only handles letters. So making sure we are ecnrypting ony letters
    for letter in message:
        new_key = (alpha.find(letter) + key) % len(alpha)
        result = result + get_cipherletter(new_key, letter)

    return result
       # if letter in alpha:  #if the letter is actually a letter encrypt it
            #find the corresponding ciphertext letter in the  alphabet.
           # letter_index = ( alpha.find(letter) + key) % len(alpha)  # shift the alphabet to left  by adding the key to the ltter
            #result = result + alpha[letter_index] # letter_index is the  postion. we get the letter by adding letter_index as n indx to the string alpha[letter_index] and add to result
        #else: # don't change it
          #  result = result + letter
    #return result

def decrypt( key,message ):
    """ function to decrypt the message """
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        new_key = (alpha.find(letter) - key) % len(alpha)
        result = result + get_cipherletter(new_key + letter)

    return result
        #if letter in alpha:
         #   letter_index = (alpha.find(letter)- key) % len(alpha)

          #  result = result + alpha[letter_index]
        #else:
         #   result = result + letter
   # return result


def main():
    word = "BILLY"

    #ecnrypt "BILLY" with a key of 3
    encrypted = encrypt(3,word)
    print(encrypted)

    decrypted = decrypt(3,encrypted)
    print(decrypted)

if __name__ == "__main__":
    main()

