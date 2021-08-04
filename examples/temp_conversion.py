file1 = open('ftemps.txt','w')
temperatures = [line.strip() for line in open('temps.txt')]
for t in temperatures:
    print(float(t)* 9/5+32, file=file1)
file1.close()
