"""
Exercise 2:
Write another program that prompts for a list of numbers as above and at the end
prints out both the maximum and minimum of the numbers instead of the average.
"""

count = 0
total = 0
numbers = list()
while True:
  line = input("Enter number here:")
  
  try: 
    
    line = int(line)
    numbers.append(line)
    total = total + line 
    count = count + 1 
    average = total / count
    maximum = max(numbers)
    minimum = min(numbers)
    
  except: 
   
    if line == "done":
      break
    else:
      print ("Invalid Input") 

#prints value of average, maximum, and minimum variable 
print ('Maximum =', maximum)
print ('Minimum =', minimum )
print ('Average =', average)
