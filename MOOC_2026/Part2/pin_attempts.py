attempts = 0

while True:
    #print("Beginning of the while block:")
    code = input("Please enter your PIN:")
    attempts += 1
    
    
   
    #print(attempts)
    #print("condition check:")
    if code == "1234":
        if attempts == 1:
            print("Correct,it took you only one single attempt")
        else:
            
            print(f"Correct!, it only took you {attempts} attempts")
        break
    else:
        print("wrong")
    

    