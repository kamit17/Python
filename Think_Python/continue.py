'''
Continue statement:
This is a control flow statement that causes the program to immediately skip
the processing of the rest of the body of the loop, for the current iteration.
But the loop still carries on running for its remaining iterations .

'''
for i in [12,16,17,24,29,30]:
    if i % 2 == 1: # if the number is odd
        continue   # Don't process it
    print(i)
print("done")