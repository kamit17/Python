1 def read_sub_snake(file):
2     infile=open(file,"r")
3     while True:
4         theline = infile.readline()
5         if len(theline) == 0:
            break
        if "snake" in theline:
            print(theline)
    infile.close()
        
read_sub_snake("snakes.txt")