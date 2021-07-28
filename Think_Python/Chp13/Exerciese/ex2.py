def read_sub_snake(file):
    infile=open(file,"r")
    while True:
        theline = infile.readline()
        if len(theline) == 0:
            break
        if "snake" in theline:
            print(theline)
    infile.close()
        
read_sub_snake("snakes.txt")