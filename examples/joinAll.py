def joinStrings(stringList):
    result =""  #initlialize the result to an empty string to store result
    for i in stringList:
        #result = result+str(i)
        result += str(i)     # The same result as above but with shorthand notation 
    return result
        
    
def main():
    print(joinStrings(['very', 'hot', 'day']))
    print(joinStrings(['this', 'is', 'it']))
    print(joinStrings(['1', '2', '3', '4', '5']))

main()