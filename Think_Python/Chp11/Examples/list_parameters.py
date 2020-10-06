def double_stuff(a_list):
    """overwrite each element in a list with double its value."""
    for (idx,val) in enumerate(a_list):
        a_list[idx] = 2 * val

things = [2,5,9]
double_stuff(things)
print(things)