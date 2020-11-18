# Write a Python program to get the smalles number from a list

def smallest_number(sample_list):
    min = sample_list[0]
    
    for i in sample_list:
        if i < min:
            min = i
    return i

print(smallest_number([1,3,5,6,-1]))