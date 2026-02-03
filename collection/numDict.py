def createDictionary():
    '''Returns a tiny Spanish dictionary'''
    number = dict()
    number['One'] = 1
    number['Two'] = 2
    number['Three'] = 3
    
    return number

def main():
    dictionary = createDictionary()
    print(dictionary['One'],dictionary['Two'],dictionary['Three'])
   

main() # run the program