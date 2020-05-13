
# Write a program that counts the number of even digits in n.

def countEvenOdd(n): 
      
    even_count = 0
    odd_count = 0
    while (n > 0): 
        rem = n % 10
        if (rem % 2 == 0): 
            even_count += 1
        else:
            odd_count += 1
              
        n = int(n / 10) 
      
    print( "Even count : " , even_count) 

  
# Drivercode 
n = 234174892374982317489374091740312; 
t = countEvenOdd(n)
  
