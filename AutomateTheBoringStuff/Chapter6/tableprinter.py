
#! /anaconda3/bin/python

#tablePrinter.py - Takes a list of strings and displays it
#in a well-organized table with each column right justified.

#tableData = [['apples','Cherries','oranges','banana'],
   #          ['Chris','Alice','Bob','Dave'],
      #       ['1','212','334543','445454']]
#

tableData = [['apples','oranges','cherries','bananas'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]


def printTable(data):
#find the longest string in each of the inner lists 
#so that the whole column can be wide enough to fit 
#all the strings
    colWidths = [0] * len(data)
    for i in colWidths:
        colWidths = max(data[i],key=len)  #using max to return the longest string
    y = len(colWidths)   #storing the max width of each column
    
    for x in range(len(data[0])):
        print(str(data[0][x]).rjust(y) +str(data[1][x]).rjust(y)+ str(data[2][x]).rjust(y)) #

printTable(tableData)
    