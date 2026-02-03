#  Write a Python program to get the frequency of the elements in a list.
import collections

list1 = [100, 75, 100, 20, 75, 12, 75, 25]
counter = collections.Counter(list1)

print("Frequency of elements in the list: ",counter)
