#Write a Python program to sum all the items in a list


def sum(list_items):
    """[summary]

    Args:
        list_items ([list]): [generates sum of list of numbers]
    """
    
    sum = 0
    for i in list_items:
        sum = i+ sum
        
    return sum


print(sum([1,2,3,4]))