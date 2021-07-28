#open the pre created test.txt and read all the lines, one at a time

mynewhandle = open("/Users/maverick/GitHub/Python/Think_Python/Chp13/Examples/test.txt")
while True: #keep reading forever
    theline=mynewhandle.readline() #Try to read next line
    if len(theline) == 0: #if there are no more lines
        break #then leave the loop
    
    #Now process the line we've just read
    print(theline,end="")
    
mynewhandle.close()  