#Write a Python program to flatten a shallow list.

lst = [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]
flatlist = []
for sublist in lst:
   for item in sublist:
      flatlist.append(item)
print (flatlist)