#Write a program that reads a text file and produces an output file which is a copy of the file, except the first five columns of each line contain a four digit line number, followed by a space. Start numbering the first line in the output file at 1. Ensure that every line number is formatted to the same width in the output file. Use one of your Python programs as test data for this exercise: your output should be a printed and numbered listing of the Python program.

#write file
"""
myfile = open("list.txt",'w')
myfile.write("dog,[snake,dog],cat\n")
myfile.write("cat\n")
myfile.write("mambo\n")
myfile.write('no.5\n')
myfile.close()
"""

#write addnumber program , which also prints the output file

def addnumber(oldfile,newfile):
    infile = open(oldfile,"r")
    outfile = open(newfile,"w")
    text = infile.readlines()
    count = 1
    for line in text:
        if count < 6:
            outfile.write(str(count) + " ")
        count += 1
        outfile.write(line)
    infile.close()
    outfile.close()
    outfile = open(newfile,'r')
    newtext = outfile.readlines()
    for i in newtext:
        print(i)
    outfile.close()
    return newtext
addnumber("ex2.py","ex2_replica.py")