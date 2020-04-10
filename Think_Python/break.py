"""The break statement is used to immediately leave the body of its loop.
The next statement to be executed is the first one after the body:"""

for i in [12,16,17,24,29]:
    if i % 2 == 1:      # if the number is odd
        break           # ...immediately exit the loop
    print(i)
print("done")