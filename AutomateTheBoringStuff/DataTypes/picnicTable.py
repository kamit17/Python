def printPicnic(itemsDict,leftWidth,rightWidth):  #function that takes in a dictinoary of information .
    print('PICNIC ITEMS'.center(leftWidth+rightWidth,'-'))
    for k,v in itemsDict.items():
        print(k.ljust(leftWidth,'-')+str(v).rjust(rightWidth))
picnicItems = {'sandwiches':4,'apples':4,'cups':12,'cookies':6000}
printPicnic(picnicItems,12,5)
printPicnic(picnicItems,20,6)