#filter that copies one file to another, omitting any lines that begin with J

def filter(oldfile,newfile):
    infile= open(oldfile,"r")
    outfile= open(newfile, "w")
    while True:
        text = infile.readline()
        if len(text) ==0:
            break
        if text[0] == "J":
            continue
        
        outfile.write(text)
        
    infile.close()
    outfile.close()

filter("friends.txt","new_list.txt")
        
