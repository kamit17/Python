attempts = 0

while True:
    print("beginning of while block:")
    code = input("Please type in your PIN: ")
    attempts += 1
    
    print("attempts: ",attempts)
    print("condition1: ",attempts)
    if code == "1234":
        success = True
        break
    
    print("code:",code)
    print("condition2:", code == "1234")
    if attempts == 3:
        success = False
        break
 # this is printed if the code was incorrect AND there have been less than three attempts
    print("Incorrect...try again")
    
if success:
    print("Correct PIN Entered!")
else:
    print("Too many attempts...")