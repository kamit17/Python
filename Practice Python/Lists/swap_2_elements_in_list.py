# Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.

def swap_position(list, pos1,pos2):
    list[pos1],list[pos2] = list[pos2],list[pos2]

    return list

list =[12,13,14,16]
pos1,pos2=1,3

print(swap_position(list,pos1-1,pos2-2))