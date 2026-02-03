''' Python program to find the
multiplication table (from 1 to 10)'''

num = int(input("Display multiplication table of? "))
max = 11
start= 1
print('_' *20)
print('The table of ',num) 
print('_'*20)
i = start
while i <=max:
    result = i*num
    print(i,'*',num,'=',result)
    i = i+1
print('_'*20)
print('Done counting')
print('_'*20)
