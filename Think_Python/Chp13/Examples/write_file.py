# simple program that writes three lines of text into a file

myfile = open("/Users/maverick/GitHub/Python/Think_Python/Chp13/Examples/test.txt", "w")
myfile.write("My first file written from Python\n")
myfile.write("---------------------------------\n")
myfile.write("Hello, world!\n")
myfile.close()
